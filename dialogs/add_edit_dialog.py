from PySide6.QtWidgets import QDialog, QMessageBox, QLineEdit, QComboBox
from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtCore import QRegularExpression
from .add_dialog_ui import Ui_dialog  # Ваш сгенерированный UI из add_dialog.ui

class AddEditDialog(QDialog):
    def __init__(self, conn, table_name, headers, record=None):
        super().__init__()
        self.ui = Ui_dialog()
        self.ui.setupUi(self)
        self.conn = conn
        self.table_name = table_name
        self.headers = headers
        self.record = record

        self.fields = {}

        # Словарь внешних ключей: поле -> (таблица, id_столбец, отображаемый_столбец)
        foreign_keys = {
            "id_отеля": ("Отели", "id_отеля", "название"),
            "id_должности": ("Должности", "id_должности", "название_должности"),
            "id_перевозчика": ("Перевозчики", "id_перевозчика", "название"),
            "id_сотрудника": ("Сотрудники", "id_сотрудника", "фио"),
            "id_клиента": ("Клиенты", "id_клиента", "фио"),
            "id_тура": ("Туры", "id_тура", "страна"),
        }

        # Для хранения данных отелей для проверки и автозаполнения
        self.hotels_data = {}

        for i, header in enumerate(headers):
            if i == 0:
                continue  # Пропускаем первичный ключ

            lname = header.lower()

            # Внешние ключи с QComboBox
            if header in foreign_keys:
                table, id_col, display_col = foreign_keys[header]
                combo = QComboBox(self)
                try:
                    with self.conn.cursor() as cur:
                        cur.execute(f'SELECT "{id_col}", "{display_col}" FROM "{table}" ORDER BY "{display_col}"')
                        items = cur.fetchall()
                    for id_val, display_val in items:
                        combo.addItem(str(display_val), id_val)
                        if header == "id_отеля":
                            with self.conn.cursor() as cur2:
                                cur2.execute(f'SELECT город, страна FROM Отели WHERE id_отеля = %s', (id_val,))
                                res = cur2.fetchone()
                                if res:
                                    self.hotels_data[id_val] = {"город": res[0], "страна": res[1]}
                except Exception as e:
                    QMessageBox.warning(self, "Ошибка", f"Не удалось загрузить данные для {header}:\n{e}")

                if record:
                    current_id = record[i]
                    index = combo.findData(current_id)
                    if index >= 0:
                        combo.setCurrentIndex(index)

                self.ui.formLayout_dialog.addRow(header, combo)
                self.fields[header] = combo

                if header == "id_отеля":
                    combo.currentIndexChanged.connect(self.on_hotel_changed)

                continue

            # Пол — QComboBox с дефолтным значением "М"
            if lname in ["пол", "gender", "sex"]:
                combo = QComboBox(self)
                combo.addItems(["М", "Ж"])
                if record:
                    value = str(record[i]) if record[i] is not None else ""
                    if value in ["М", "Ж"]:
                        combo.setCurrentText(value)
                    else:
                        combo.setCurrentIndex(0)
                else:
                    combo.setCurrentIndex(0)
                self.ui.formLayout_dialog.addRow(header, combo)
                self.fields[header] = combo
                continue

            # Питание — QComboBox с двумя вариантами True/False
            if lname in ["питание", "meal", "питание_в_отеле"]:
                combo = QComboBox(self)
                combo.addItems(["True", "False"])
                if record:
                    value = str(record[i]) if record[i] is not None else ""
                    if value in combo.model().stringList():
                        combo.setCurrentText(value)
                    else:
                        combo.setCurrentIndex(0)
                else:
                    combo.setCurrentIndex(0)
                self.ui.formLayout_dialog.addRow(header, combo)
                self.fields[header] = combo
                continue

            line_edit = QLineEdit(self)

            if "дата" in lname or "date" in lname:
                date_regex = QRegularExpression(r"\d{2} \d{2} \d{4}")
                date_validator = QRegularExpressionValidator(date_regex)
                line_edit.setValidator(date_validator)
                line_edit.setPlaceholderText("ДД ММ ГГГГ (например, 31 12 2023)")

            elif "телефон" in lname or "phone" in lname:
                line_edit.setInputMask("+7 (000) 000-00-00")

            elif "паспорт" in lname:
                passport_regex = QRegularExpression(r"\d{4} \d{6}")
                passport_validator = QRegularExpressionValidator(passport_regex)
                line_edit.setValidator(passport_validator)
                line_edit.setPlaceholderText("1234 567890")

            elif "инн" in lname:
                inn_regex = QRegularExpression(r"\d{12}")
                inn_validator = QRegularExpressionValidator(inn_regex)
                line_edit.setValidator(inn_validator)
                line_edit.setPlaceholderText("12 цифр, например 123456789012")

            if record:
                value = str(record[i]) if record[i] is not None else ""
                line_edit.setText(value)

            self.ui.formLayout_dialog.addRow(header, line_edit)
            self.fields[header] = line_edit

        # Сохраняем ссылки на поля города и страны для таблицы Туры
        self.city_field = self.fields.get("город")
        self.country_field = self.fields.get("страна")

        self.ui.btn_save.clicked.connect(self.save_data)
        self.ui.btn_cancel.clicked.connect(self.reject)

        # При инициализации, если редактируем и есть отель, подставляем город и страну
        if self.table_name == "Туры" and record and "id_отеля" in self.fields:
            hotel_combo = self.fields["id_отеля"]
            current_id = hotel_combo.currentData()
            self.fill_city_country(current_id)

    def on_hotel_changed(self, index):
        combo = self.fields.get("id_отеля")
        if combo:
            hotel_id = combo.itemData(index)
            if self.table_name == "Туры":
                self.fill_city_country(hotel_id)

    def fill_city_country(self, hotel_id):
        if hotel_id in self.hotels_data:
            hotel_info = self.hotels_data[hotel_id]
            city = hotel_info.get("город", "")
            country = hotel_info.get("страна", "")
            if self.city_field and self.country_field:
                # Берём текущие значения для города и страны
                current_city = self.city_field.text()
                current_country = self.country_field.text()
                # Если они отличаются от данных отеля, заменяем на данные отеля
                if current_city != city or current_country != country:
                    self.city_field.setText(city)
                    self.country_field.setText(country)

    def save_data(self):
        try:
            with self.conn.cursor() as cur:
                # Перед сохранением для таблицы Туры проверяем город и страну
                if self.table_name == "Туры" and "id_отеля" in self.fields:
                    hotel_id = self.fields["id_отеля"].currentData()
                    if hotel_id in self.hotels_data:
                        hotel_city = self.hotels_data[hotel_id]["город"]
                        hotel_country = self.hotels_data[hotel_id]["страна"]
                        # Принудительно подставляем город и страну из отеля
                        if "город" in self.fields:
                            self.fields["город"].setText(hotel_city)
                        if "страна" in self.fields:
                            self.fields["страна"].setText(hotel_country)

                if self.record:
                    set_clause = ", ".join([f'"{h}" = %s' for h in self.fields.keys()])
                    query = f'UPDATE "{self.table_name}" SET {set_clause} WHERE "{self.headers[0]}" = %s'
                    values = []
                    for h in self.fields:
                        widget = self.fields[h]
                        if isinstance(widget, QComboBox):
                            val = widget.currentText()
                            if not val and (h.lower() in ["пол", "gender", "sex"]):
                                val = "М"
                            if h in ["id_отеля", "id_должности", "id_перевозчика", "id_сотрудника", "id_клиента", "id_тура"]:
                                val = widget.currentData()
                            values.append(val)
                        else:
                            values.append(widget.text())
                    values.append(self.record[0])
                    cur.execute(query, values)
                else:
                    columns = ", ".join([f'"{h}"' for h in self.fields.keys()])
                    placeholders = ", ".join(["%s"] * len(self.fields))
                    query = f'INSERT INTO "{self.table_name}" ({columns}) VALUES ({placeholders})'
                    values = []
                    for h in self.fields:
                        widget = self.fields[h]
                        if isinstance(widget, QComboBox):
                            val = widget.currentText()
                            if not val and (h.lower() in ["пол", "gender", "sex"]):
                                val = "М"
                            if h in ["id_отеля", "id_должности", "id_перевозчика", "id_сотрудника", "id_клиента", "id_тура"]:
                                val = widget.currentData()
                            values.append(val)
                        else:
                            values.append(widget.text())
                    cur.execute(query, values)
                self.conn.commit()
            self.accept()
        except Exception as e:
            self.conn.rollback()
            QMessageBox.critical(self, "Ошибка", f"Ошибка при сохранении данных:\n{e}")
