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

        # Загрузим данные отелей с городом и страной для автозаполнения
        self.hotels_data = {}
        try:
            with self.conn.cursor() as cur:
                cur.execute('SELECT id_отеля, город, страна FROM Отели')
                for id_val, city, country in cur.fetchall():
                    self.hotels_data[id_val] = {"город": city, "страна": country}
        except Exception as e:
            QMessageBox.warning(self, "Внимание", f"Не удалось загрузить данные отелей для автозаполнения:\n{e}")

        # Словарь внешних ключей: поле -> (таблица, id_столбец, отображаемый_столбец)
        foreign_keys = {
            "id_отеля": ("Отели", "id_отеля", "название"),
            "id_должности": ("Должности", "id_должности", "название_должности"),
            "id_перевозчика": ("Перевозчики", "id_перевозчика", "название"),
            "id_сотрудника": ("Сотрудники", "id_сотрудника", "ФИО"),
            "id_клиента": ("Клиенты", "id_клиента", "ФИО"),
        }

        for i, header in enumerate(headers):
            if i == 0 and self.table_name != "Экскурсии_Туры":
                continue  # Пропускаем первичный ключ для всех таблиц, кроме Экскурсии_Туры

            lname = header.lower()

            # Особая обработка для таблицы Экскурсии_Туры
            if self.table_name == "Экскурсии_Туры":
                if header == "id_тура":
                    combo = QComboBox(self)
                    with self.conn.cursor() as cur:
                        cur.execute('SELECT id_тура, страна, город FROM Туры ORDER BY страна, город')
                        tours = cur.fetchall()
                    for id_val, country, city in tours:
                        combo.addItem(f"{id_val} — {country}, {city}", id_val)
                    if record:
                        current_id = record[i]
                        index = combo.findData(current_id)
                        if index >= 0:
                            combo.setCurrentIndex(index)
                    self.ui.formLayout_dialog.addRow("id_тура", combo)
                    self.fields["id_тура"] = combo
                    continue

                if header == "id_экскурсии":
                    combo = QComboBox(self)
                    with self.conn.cursor() as cur:
                        cur.execute('SELECT id_экскурсии, название FROM Экскурсии ORDER BY название')
                        excursions = cur.fetchall()
                    for id_val, name in excursions:
                        combo.addItem(name, id_val)
                    if record:
                        current_id = record[i]
                        index = combo.findData(current_id)
                        if index >= 0:
                            combo.setCurrentIndex(index)
                    self.ui.formLayout_dialog.addRow("id_экскурсии", combo)
                    self.fields["id_экскурсии"] = combo
                    continue

            # Внешние ключи для остальных таблиц
            if header in foreign_keys:
                table, id_col, display_col = foreign_keys[header]
                combo = QComboBox(self)
                with self.conn.cursor() as cur:
                    cur.execute(f'SELECT "{id_col}", "{display_col}" FROM "{table}" ORDER BY "{display_col}"')
                    items = cur.fetchall()
                for id_val, display_val in items:
                    combo.addItem(str(display_val), id_val)
                if record:
                    current_id = record[i]
                    index = combo.findData(current_id)
                    if index >= 0:
                        combo.setCurrentIndex(index)
                self.ui.formLayout_dialog.addRow(header, combo)
                self.fields[header] = combo

                # Если поле id_отеля — подключаем автозаполнение города и страны
                if header == "id_отеля":
                    combo.currentIndexChanged.connect(self.on_hotel_changed)
                continue

            # Валидаторы для других полей
            validator, placeholder = self.get_validator_and_placeholder(lname)
            line_edit = QLineEdit(self)
            if validator:
                line_edit.setValidator(validator)
            if placeholder:
                line_edit.setPlaceholderText(placeholder)
            if record:
                value = str(record[i]) if record[i] is not None else ""
                line_edit.setText(value)
            self.ui.formLayout_dialog.addRow(header, line_edit)
            self.fields[header] = line_edit

        # Сохраняем ссылки на поля город и страна, если они есть
        self.city_field = self.fields.get("город")
        self.country_field = self.fields.get("страна")

        # Если редактируем тур и уже выбран отель — сразу автозаполняем
        if self.table_name == "Туры" and record and "id_отеля" in self.fields:
            hotel_combo = self.fields["id_отеля"]
            current_id = hotel_combo.currentData()
            self.fill_city_country(current_id)

        self.ui.btn_save.clicked.connect(self.save_data)
        self.ui.btn_cancel.clicked.connect(self.reject)

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
                current_city = self.city_field.text()
                current_country = self.country_field.text()
                if current_city != city or current_country != country:
                    self.city_field.setText(city)
                    self.country_field.setText(country)

    def get_validator_and_placeholder(self, lname):
        if "дата" in lname or "date" in lname:
            regex = QRegularExpression(r"\d{2} \d{2} \d{4}")
            return QRegularExpressionValidator(regex), "ДД ММ ГГГГ (например, 31 12 2023)"
        elif "телефон" in lname or "phone" in lname:
            return None, "+7 (___) ___-__-__"
        elif "паспорт" in lname:
            regex = QRegularExpression(r"\d{4} \d{6}")
            return QRegularExpressionValidator(regex), "1234 567890"
        elif "инн" in lname:
            regex = QRegularExpression(r"\d{12}")
            return QRegularExpressionValidator(regex), "12 цифр, например 123456789012"
        else:
            return None, None

    def save_data(self):
        try:
            with self.conn.cursor() as cur:
                # Автозаполнение города и страны перед сохранением (если тур)
                if self.table_name == "Туры" and "id_отеля" in self.fields:
                    hotel_id = self.fields["id_отеля"].currentData()
                    if hotel_id in self.hotels_data:
                        hotel_city = self.hotels_data[hotel_id]["город"]
                        hotel_country = self.hotels_data[hotel_id]["страна"]
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
