from PySide6.QtWidgets import QDialog, QMessageBox, QLineEdit, QComboBox
from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtCore import QRegularExpression
from datetime import datetime
from decimal import Decimal
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

        # Загрузим данные отелей с городом, страной и ценой для автозаполнения
        self.hotels_data = {}
        try:
            with self.conn.cursor() as cur:
                cur.execute('SELECT id_отеля, город, страна, цена FROM Отели')
                for id_val, city, country, price in cur.fetchall():
                    self.hotels_data[id_val] = {"город": city, "страна": country, "цена": price}
        except Exception as e:
            QMessageBox.warning(self, "Внимание", f"Не удалось загрузить данные отелей:\n{e}")

        # Загрузим цены перевозчиков
        self.carriers_price = {}
        try:
            with self.conn.cursor() as cur:
                cur.execute('SELECT id_перевозчика, цена FROM Перевозчики')
                for id_val, price in cur.fetchall():
                    self.carriers_price[id_val] = price
        except Exception as e:
            QMessageBox.warning(self, "Внимание", f"Не удалось загрузить данные перевозчиков:\n{e}")

        # Внешние ключи
        foreign_keys = {
            "id_отеля": ("Отели", "id_отеля", "название"),
            "id_должности": ("Должности", "id_должности", "название_должности"),
            "id_перевозчика": ("Перевозчики", "id_перевозчика", "название"),
            "id_сотрудника": ("Сотрудники", "id_сотрудника", "ФИО"),
            "id_клиента": ("Клиенты", "id_клиента", "ФИО"),
        }


        for i, header in enumerate(headers):
            if i == 0 and self.table_name != "Экскурсии_Туры":
                continue  # Пропускаем PK

            # --- Новый блок: обработка продолжительности тура ---
            if header == "продолжительность_дней":
                line_edit = QLineEdit(self)
                line_edit.setValidator(QRegularExpressionValidator(QRegularExpression(r"\d+")))
                if record:
                    line_edit.setText(str(record[i]))
                self.ui.formLayout_dialog.addRow(header, line_edit)
                self.fields[header] = line_edit
                continue

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

                if header == "id_отеля":
                    combo.currentIndexChanged.connect(self.on_hotel_changed)
                continue

            # Для поля статус_оплаты добавим подсказку и ограничим ввод (true/false)
            if header == "статус_оплаты":
                combo = QComboBox(self)
                combo.addItem("True", True)
                combo.addItem("False", False)
                if record:
                    current_val = record[i]
                    index = combo.findData(current_val)
                    if index >= 0:
                        combo.setCurrentIndex(index)
                combo.setToolTip("Выберите True, если оплата произведена, иначе False")
                self.ui.formLayout_dialog.addRow(header, combo)
                self.fields[header] = combo
                continue

            # Валидаторы для других полей
            validator, placeholder = self.get_validator_and_placeholder(lname)
            line_edit = QLineEdit(self)
            if validator:
                line_edit.setValidator(validator)
            if placeholder:
                line_edit.setPlaceholderText(placeholder)
            if record:
                value = record[i]
                # Если поле дата, преобразуем из ISO в ДД ММ ГГГГ для отображения
                if value is not None and ("дата" in header.lower()):
                    try:
                        dt = datetime.strptime(str(value), "%Y-%m-%d")
                        value = dt.strftime("%d %m %Y")
                    except ValueError:
                        value = str(value)
                else:
                    value = str(value) if value is not None else ""
                line_edit.setText(value)
            self.ui.formLayout_dialog.addRow(header, line_edit)
            self.fields[header] = line_edit

        self.city_field = self.fields.get("город")
        self.country_field = self.fields.get("страна")

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

    def _get_field_value(self, widget, field_name=None):
        if isinstance(widget, QComboBox):
            return widget.currentData()
        elif isinstance(widget, QLineEdit):
            text = widget.text().strip()
            if field_name and ("дата" in field_name.lower() or "date" in field_name.lower()):
                return text if text else None
            return text
        return widget

    def calculate_tour_price(self, id_тура):
        """Вычисляет стоимость тура по формуле и возвращает число или None."""
        try:
            with self.conn.cursor() as cur:
                cur.execute('SELECT продолжительность_дней, id_отеля, id_перевозчика FROM Туры WHERE id_тура = %s', (id_тура,))
                row = cur.fetchone()
                if not row:
                    return None
                duration, id_отеля, id_перевозчика = row

                price_hotel = Decimal('0')
                if id_отеля is not None:
                    cur.execute('SELECT цена FROM Отели WHERE id_отеля = %s', (id_отеля,))
                    res = cur.fetchone()
                    if res and res[0] is not None:
                        price_hotel = Decimal(res[0])

                price_carrier = Decimal('0')
                if id_перевозчика is not None:
                    cur.execute('SELECT цена FROM Перевозчики WHERE id_перевозчика = %s', (id_перевозчика,))
                    res = cur.fetchone()
                    if res and res[0] is not None:
                        price_carrier = Decimal(res[0])

                cur.execute('''
                    SELECT COALESCE(SUM(Экскурсии.цена), 0)
                    FROM Экскурсии_Туры
                    JOIN Экскурсии ON Экскурсии_Туры.id_экскурсии = Экскурсии.id_экскурсии
                    WHERE Экскурсии_Туры.id_тура = %s
                ''', (id_тура,))
                price_excursions_raw = cur.fetchone()[0]
                price_excursions = Decimal(price_excursions_raw) if price_excursions_raw is not None else Decimal('0')

                duration_dec = Decimal(duration) if duration is not None else Decimal('0')

                total_price = (price_hotel * duration_dec) + price_carrier + price_excursions
                total_price *= Decimal('1.2')

                return round(total_price, 2)
        except Exception as e:
            QMessageBox.warning(self, "Ошибка", f"Ошибка при вычислении стоимости тура:\n{e}")
            return None

    def recalc_and_update_tour_price(self, id_тура):
        """Пересчитывает и обновляет цену тура в базе."""
        price = self.calculate_tour_price(id_тура)
        if price is not None:
            try:
                with self.conn.cursor() as cur:
                    cur.execute('UPDATE "Туры" SET цена = %s WHERE id_тура = %s', (price, id_тура))
                self.conn.commit()
            except Exception as e:
                self.conn.rollback()
                QMessageBox.warning(self, "Ошибка", f"Ошибка при обновлении цены тура:\n{e}")

    def delete_excursion_tour_pair(self, id_тура, id_экскурсии):
        """Удаляет из Экскурсии_Туры конкретную пару (id_тура, id_экскурсии)."""
        try:
            with self.conn.cursor() as cur:
                cur.execute(
                    'DELETE FROM "Экскурсии_Туры" WHERE id_тура = %s AND id_экскурсии = %s',
                    (id_тура, id_экскурсии)
                )
            self.conn.commit()
            # После удаления пересчитываем цену тура
            self.recalc_and_update_tour_price(id_тура)
        except Exception as e:
            self.conn.rollback()
            QMessageBox.critical(self, "Ошибка", f"Ошибка при удалении записи:\n{e}")

    def save_data(self):
        try:
            # Проверки для Договоры_клиенты (оставляем как есть)
            if self.table_name == "Договоры_клиенты":
                дата_оплаты_widget = self.fields.get("дата_оплаты")
                статус_оплаты_widget = self.fields.get("статус_оплаты")

                дата_оплаты = None
                if isinstance(дата_оплаты_widget, QLineEdit):
                    дата_оплаты = дата_оплаты_widget.text().strip()
                    if дата_оплаты == "":
                        дата_оплаты = None

                статус_оплаты = None
                if статус_оплаты_widget:
                    if isinstance(статус_оплаты_widget, QComboBox):
                        статус_оплаты = статус_оплаты_widget.currentData()
                    elif isinstance(статус_оплаты_widget, QLineEdit):
                        статус_оплаты = статус_оплаты_widget.text().lower() in ("true", "1", "да", "истина", "yes")

                if дата_оплаты is not None and not статус_оплаты:
                    QMessageBox.critical(self, "Ошибка", "Если дата оплаты указана, статус оплаты должен быть True.")
                    return

                if дата_оплаты is None and статус_оплаты:
                    QMessageBox.critical(self, "Ошибка", "Если дата оплаты не указана, статус оплаты не может быть True.")
                    return

                дата_подписания_widget = self.fields.get("дата_подписания")
                дата_подписания = None
                if isinstance(дата_подписания_widget, QLineEdit):
                    дата_подписания = дата_подписания_widget.text().strip()
                    if дата_подписания == "":
                        дата_подписания = None

                if дата_оплаты and дата_подписания:
                    try:
                        dt_оплаты = datetime.strptime(дата_оплаты, "%d %m %Y")
                        dt_подписания = datetime.strptime(дата_подписания, "%d %m %Y")
                        if dt_оплаты <= dt_подписания:
                            QMessageBox.critical(self, "Ошибка", "Дата оплаты должна быть позже даты подписания.")
                            return
                    except ValueError as e:
                        QMessageBox.critical(self, "Ошибка", f"Ошибка при проверке дат: {e}")
                        return

            with self.conn.cursor() as cur:
                if self.table_name == "Туры":
                    id_тура = None
                    columns = []
                    values = []

                    for h in self.fields:
                        if h == "цена":
                            continue
                        widget = self.fields[h]
                        val = self._get_field_value(widget, h)
                        columns.append(f'"{h}"')
                        values.append(val)

                    if self.record:
                        id_тура = self.record[0]
                        set_clause = ", ".join([f'"{h}" = %s' for h in self.fields.keys() if h != "цена"])
                        query = f'UPDATE "{self.table_name}" SET {set_clause} WHERE "{self.headers[0]}" = %s'
                        cur.execute(query, values + [id_тура])
                    else:
                        placeholders = ", ".join(["%s"] * len(values))
                        query = f'INSERT INTO "{self.table_name}" ({", ".join(columns)}) VALUES ({placeholders}) RETURNING "{self.headers[0]}"'
                        cur.execute(query, values)
                        id_тура = cur.fetchone()[0]

                    self.recalc_and_update_tour_price(id_тура)

                elif self.table_name == "Экскурсии_Туры":
                    if self.record:
                        set_clause = ", ".join([f'"{h}" = %s' for h in self.fields.keys()])
                        query = f'UPDATE "{self.table_name}" SET {set_clause} WHERE "{self.headers[0]}" = %s'
                        values = []
                        for h in self.fields:
                            widget = self.fields[h]
                            values.append(self._get_field_value(widget, h))
                        values.append(self.record[0])
                        cur.execute(query, values)
                    else:
                        columns = ", ".join([f'"{h}"' for h in self.fields.keys()])
                        placeholders = ", ".join(["%s"] * len(self.fields))
                        query = f'INSERT INTO "{self.table_name}" ({columns}) VALUES ({placeholders})'
                        values = []
                        for h in self.fields:
                            widget = self.fields[h]
                            values.append(self._get_field_value(widget, h))
                        cur.execute(query, values)

                    id_тура = None
                    if "id_тура" in self.fields:
                        id_тура = self.fields["id_тура"].currentData()
                    if id_тура:
                        self.recalc_and_update_tour_price(id_тура)

                elif self.table_name == "Экскурсии":
                    if self.record:
                        set_clause = ", ".join([f'"{h}" = %s' for h in self.fields.keys()])
                        query = f'UPDATE "{self.table_name}" SET {set_clause} WHERE "{self.headers[0]}" = %s'
                        values = []
                        for h in self.fields:
                            widget = self.fields[h]
                            values.append(self._get_field_value(widget, h))
                        values.append(self.record[0])
                        cur.execute(query, values)
                    else:
                        columns = ", ".join([f'"{h}"' for h in self.fields.keys()])
                        placeholders = ", ".join(["%s"] * len(self.fields))
                        query = f'INSERT INTO "{self.table_name}" ({columns}) VALUES ({placeholders})'
                        values = []
                        for h in self.fields:
                            widget = self.fields[h]
                            values.append(self._get_field_value(widget, h))
                        cur.execute(query, values)

                    id_экскурсии = self.record[0] if self.record else None
                    if id_экскурсии is None:
                        id_экскурсии = cur.fetchone()[0]

                    cur.execute('SELECT DISTINCT id_тура FROM Экскурсии_Туры WHERE id_экскурсии = %s', (id_экскурсии,))
                    tours = cur.fetchall()
                    for (id_тура,) in tours:
                        self.recalc_and_update_tour_price(id_тура)

                elif self.table_name == "Перевозчики":
                    if self.record:
                        set_clause = ", ".join([f'"{h}" = %s' for h in self.fields.keys()])
                        query = f'UPDATE "{self.table_name}" SET {set_clause} WHERE "{self.headers[0]}" = %s'
                        values = []
                        for h in self.fields:
                            widget = self.fields[h]
                            values.append(self._get_field_value(widget, h))
                        values.append(self.record[0])
                        cur.execute(query, values)
                    else:
                        columns = ", ".join([f'"{h}"' for h in self.fields.keys()])
                        placeholders = ", ".join(["%s"] * len(self.fields))
                        query = f'INSERT INTO "{self.table_name}" ({columns}) VALUES ({placeholders})'
                        values = []
                        for h in self.fields:
                            widget = self.fields[h]
                            values.append(self._get_field_value(widget, h))
                        cur.execute(query, values)

                    id_перевозчика = self.record[0] if self.record else None
                    if id_перевозчика is None:
                        id_перевозчика = cur.fetchone()[0]

                    cur.execute('SELECT id_тура FROM Туры WHERE id_перевозчика = %s', (id_перевозчика,))
                    tours = cur.fetchall()
                    for (id_тура,) in tours:
                        self.recalc_and_update_tour_price(id_тура)

                elif self.table_name == "Отели":
                    if self.record:
                        set_clause = ", ".join([f'"{h}" = %s' for h in self.fields.keys()])
                        query = f'UPDATE "{self.table_name}" SET {set_clause} WHERE "{self.headers[0]}" = %s'
                        values = []
                        for h in self.fields:
                            widget = self.fields[h]
                            values.append(self._get_field_value(widget, h))
                        values.append(self.record[0])
                        cur.execute(query, values)
                    else:
                        columns = ", ".join([f'"{h}"' for h in self.fields.keys()])
                        placeholders = ", ".join(["%s"] * len(self.fields))
                        query = f'INSERT INTO "{self.table_name}" ({columns}) VALUES ({placeholders})'
                        values = []
                        for h in self.fields:
                            widget = self.fields[h]
                            values.append(self._get_field_value(widget, h))
                        cur.execute(query, values)

                    id_отеля = self.record[0] if self.record else None
                    if id_отеля is None:
                        id_отеля = cur.fetchone()[0]

                    cur.execute('SELECT id_тура FROM Туры WHERE id_отеля = %s', (id_отеля,))
                    tours = cur.fetchall()
                    for (id_тура,) in tours:
                        self.recalc_and_update_tour_price(id_тура)

                else:
                    if self.record:
                        set_clause = ", ".join([f'"{h}" = %s' for h in self.fields.keys()])
                        query = f'UPDATE "{self.table_name}" SET {set_clause} WHERE "{self.headers[0]}" = %s'
                        values = []
                        for h in self.fields:
                            widget = self.fields[h]
                            values.append(self._get_field_value(widget, h))
                        values.append(self.record[0])
                        cur.execute(query, values)
                    else:
                        columns = ", ".join([f'"{h}"' for h in self.fields.keys()])
                        placeholders = ", ".join(["%s"] * len(self.fields))
                        query = f'INSERT INTO "{self.table_name}" ({columns}) VALUES ({placeholders})'
                        values = []
                        for h in self.fields:
                            widget = self.fields[h]
                            values.append(self._get_field_value(widget, h))
                        cur.execute(query, values)

                self.conn.commit()
            self.accept()
        except Exception as e:
            self.conn.rollback()
            QMessageBox.critical(self, "Ошибка", f"Ошибка при сохранении данных:\n{e}")
