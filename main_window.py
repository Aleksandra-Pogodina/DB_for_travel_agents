from PySide6.QtWidgets import (
    QMainWindow, QMessageBox, QAbstractItemView, QDialog, QLineEdit
)
from PySide6.QtCore import QAbstractTableModel, Qt, QSortFilterProxyModel
from main_window_ui import Ui_MainWindow
import db
import reports
from dialogs.add_edit_dialog import AddEditDialog  # Универсальный диалог


class TableModel(QAbstractTableModel):
    def __init__(self, data, headers):
        super().__init__()
        self._data = data
        self._headers = headers

    def rowCount(self, parent=None):
        return len(self._data)

    def columnCount(self, parent=None):
        return len(self._headers)

    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            return str(self._data[index.row()][index.column()])
        return None

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return self._headers[section]
            else:
                return str(section + 1)
        return None


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Устанавливаем флаги окна: убрать кнопку максимизации, но оставить закрытие и изменение размера
        self.setWindowFlags(
            Qt.Window |
            Qt.WindowMinimizeButtonHint |
            Qt.WindowCloseButtonHint |
            Qt.WindowSystemMenuHint
        )

        # Очищаем стили у таблиц, чтобы убрать чёрный фон (если был)
        self.ui.tableView_table.setStyleSheet("")
        self.ui.tableView_report.setStyleSheet("")

        # Настройка таблиц — выбор и запрет редактирования
        self.ui.tableView_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.tableView_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.tableView_table.horizontalHeader().setVisible(True)
        self.ui.tableView_table.verticalHeader().setVisible(True)

        self.ui.tableView_report.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.tableView_report.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.tableView_report.horizontalHeader().setVisible(True)
        self.ui.tableView_report.verticalHeader().setVisible(True)

        # Стиль для заголовков и углового квадрата с прозрачным тёмным фоном и рамкой
        header_style = """
        QHeaderView::section {
            background-color: rgba(43, 43, 43, 0.7);
            color: #f0f0f0;
            border: 1px solid #555555;
            padding: 4px;
            box-sizing: border-box;
        }
        QTableCornerButton {
            background-color: rgba(43, 43, 43, 0.7);
            border: 1px solid #555555;
        }
        """
        self.ui.tableView_table.horizontalHeader().setStyleSheet(header_style)
        self.ui.tableView_table.verticalHeader().setStyleSheet(header_style)
        self.ui.tableView_report.horizontalHeader().setStyleSheet(header_style)
        self.ui.tableView_report.verticalHeader().setStyleSheet(header_style)

        # Подключение к базе данных
        self.conn = db.test_connection()
        if not self.conn:
            QMessageBox.critical(self, "Ошибка подключения", "Не удалось подключиться к базе данных!")
            exit(1)

        # Устанавливаем схему по умолчанию для сессии
        try:
            with self.conn.cursor() as cur:
                cur.execute('SET search_path TO курсовая;')
                self.conn.commit()
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось установить схему:\n{e}")
            exit(1)

        # Списки таблиц и отчётов
        self.table_names = [
            "Должности", "Сотрудники", "Клиенты", "Отели", "Перевозчики",
            "Экскурсии", "Туры", "Экскурсии_Туры", "Договоры_клиенты",
            "Договоры_партнёры_отели", "Договоры_партнёры_перевозчики",
            "Договоры_партнёры_экскурсии"
        ]

        self.ui.comboBox_table.clear()
        self.ui.comboBox_table.addItems(self.table_names)
        self.ui.comboBox_table.currentIndexChanged.connect(self.load_table_data)

        self.report_names = [
            "Все туры с отелем и перевозчиком", "Клиенты с количеством покупок",
            "Экскурсии для туров", "Договоры с клиентами, турами и сотрудниками",
            "Сотрудники с должностями и окладами", "Договоры с отелями и сотрудниками",
            "Договоры с экскурсиями и сотрудниками", "Договоры с перевозчиками и сотрудниками",
            "Договоры с неоплаченным статусом", "Статистика цен туров по странам",
            "Отели с питанием и вместимостью", "Количество договоров по сотрудникам",
            "Клиенты без покупок", "Туры с количеством экскурсий", "Общая выручка по турам"
        ]

        self.ui.comboBox_report.clear()
        self.ui.comboBox_report.addItems(self.report_names)
        self.ui.comboBox_report.currentIndexChanged.connect(self.load_report)

        # Навигация по страницам
        self.ui.btn_Clients.clicked.connect(self.show_report_page)
        self.ui.btn_Tours.clicked.connect(self.show_table_page)
        self.ui.btn_back_on_report.clicked.connect(self.show_main_page)
        self.ui.btn_back_on_table.clicked.connect(self.show_main_page)

        # Кнопки управления таблицами
        self.ui.btn_add.clicked.connect(self.add_record)
        self.ui.btn_change.clicked.connect(self.edit_record)
        self.ui.btn_delete.clicked.connect(self.delete_record)

        # === Добавлено: Поиск по таблице ===
        self.proxy_model = QSortFilterProxyModel(self)
        self.proxy_model.setFilterCaseSensitivity(Qt.CaseInsensitive)
        self.proxy_model.setFilterKeyColumn(-1)  # Поиск по всем колонкам

        # Устанавливаем прокси-модель в таблицу
        self.ui.tableView_table.setModel(self.proxy_model)

        # Подключаем сигнал изменения текста в поле поиска к фильтру прокси-модели
        self.ui.lineEdit_search.textChanged.connect(self.proxy_model.setFilterFixedString)
        # === Конец добавления поиска ===

        # Загрузка данных при старте
        self.ui.comboBox_table.setCurrentIndex(0)
        self.load_table_data(0)
        self.ui.comboBox_report.setCurrentIndex(0)
        self.load_report(0)
        self.show_main_page()

    def show_main_page(self):
        self.ui.pages.setCurrentWidget(self.ui.mainpage)

    def show_report_page(self):
        self.ui.pages.setCurrentWidget(self.ui.report_page)
        self.load_report(self.ui.comboBox_report.currentIndex())

    def show_table_page(self):
        self.ui.pages.setCurrentWidget(self.ui.table_page)
        self.load_table_data(self.ui.comboBox_table.currentIndex())

    def load_table_data(self, index):
        if index < 0 or index >= len(self.table_names):
            return

        self.ui.lineEdit_search.clear()

        table_name = self.table_names[index]
        try:
            with self.conn.cursor() as cur:
                cur.execute(f'SELECT * FROM "{table_name}";')
                data = cur.fetchall()
                headers = [desc[0] for desc in cur.description]
                model = TableModel(data, headers)
                # Обновляем источник данных прокси-модели
                self.proxy_model.setSourceModel(model)
                self.ui.tableView_table.resizeColumnsToContents()
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Ошибка загрузки таблицы:\n{e}")

    def load_report(self, index):
        report_functions = [
            reports.get_all_tours_with_hotel_and_carrier,
            reports.get_clients_with_purchase_count,
            reports.get_excursions_for_tours,
            reports.get_contracts_with_client_tour_employee,
            reports.get_employees_with_positions_and_salaries,
            reports.get_hotel_contracts_with_employee,
            reports.get_excursion_contracts_with_employee,
            reports.get_carrier_contracts_with_employee,
            reports.get_unpaid_contracts,
            reports.get_tour_price_stats_by_country,
            reports.get_hotels_with_meals_and_capacity,
            reports.get_contract_count_by_employee,
            reports.get_clients_with_no_purchases,
            reports.get_tours_with_excursion_counts,
            reports.get_total_revenue_per_tour,
        ]

        if index < 0 or index >= len(report_functions):
            return

        func = report_functions[index]
        try:
            data = func(self.conn)
            if not data:
                QMessageBox.information(self, "Отчёт", "Данные отсутствуют.")
                self.ui.tableView_report.setModel(None)
                return

            headers_map = {
                0: ["ID тура", "Страна", "Город", "Продолжительность (дней)", "Цена", "Отель", "Перевозчик"],
                1: ["ФИО", "Телефон", "Количество покупок"],
                2: ["Страна тура", "Город", "Название экскурсии", "Тип", "Продолжительность (часов)", "Описание", "Цена"],
                3: ["ID договора", "Клиент", "Страна", "Город", "Сотрудник", "Дата подписания", "Статус оплаты"],
                4: ["ФИО", "Должность", "Оклад", "Дата рождения", "Пол", "Телефон", "Паспорт", "ИНН"],
                5: ["ID договора", "Название отеля", "Цена", "Дата подписания", "Дата окончания", "Сотрудник"],
                6: ["ID договора", "Название экскурсии", "Цена", "Дата подписания", "Дата окончания", "Сотрудник"],
                7: ["ID договора", "Перевозчик", "Цена", "Дата подписания", "Дата окончания", "Сотрудник"],
                8: ["ID договора", "Клиент", "Страна", "Город", "Дата подписания"],
                9: ["Страна", "Средняя цена", "Минимальная цена", "Максимальная цена"],
                10: ["Название", "Страна", "Город", "Мак. вместимость номера"],
                11: ["ФИО", "Количество договоров"],
                12: ["ФИО", "Телефон"],
                13: ["ID тура", "Страна", "Город", "Количество экскурсий"],
                14: ["ID тура", "Страна", "Город", "Цена тура", "Цена перевозчика", "Цена отеля", "Сумма экскурсий", "Общая выручка"],
            }

            headers = headers_map.get(index, [])
            model = TableModel(data, headers)
            self.ui.tableView_report.setModel(model)
            self.ui.tableView_report.resizeColumnsToContents()
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Ошибка загрузки отчёта:\n{e}")

    def add_record(self):
        table_index = self.ui.comboBox_table.currentIndex()
        table = self.table_names[table_index]
        model = self.ui.tableView_table.model()
        if model and hasattr(model, '_headers') and model._headers:
            headers = model._headers
        else:
            headers = self.get_table_headers(table)
        if not headers:
            QMessageBox.warning(self, "Ошибка", "Не удалось получить структуру таблицы для добавления.")
            return
        dialog = AddEditDialog(self.conn, table, headers)
        if dialog.exec() == QDialog.Accepted:
            self.load_table_data(table_index)

    def edit_record(self):
        selection_model = self.ui.tableView_table.selectionModel()
        if not selection_model.hasSelection():
            QMessageBox.warning(self, "Изменить", "Выберите запись для изменения.")
            return
        row = selection_model.selectedRows()[0].row()
        model = self.ui.tableView_table.model()
        record = model._data[row]
        headers = model._headers
        table_index = self.ui.comboBox_table.currentIndex()
        table = self.table_names[table_index]
        dialog = AddEditDialog(self.conn, table, headers, record=record)
        if dialog.exec() == QDialog.Accepted:
            self.load_table_data(table_index)

    def delete_record(self):
        selection_model = self.ui.tableView_table.selectionModel()
        if not selection_model.hasSelection():
            QMessageBox.warning(self, "Удалить", "Выберите запись для удаления.")
            return
        selected_indexes = selection_model.selectedRows()
        if not selected_indexes:
            QMessageBox.warning(self, "Удалить", "Выберите запись для удаления.")
            return
        row = selected_indexes[0].row()
        model = self.ui.tableView_table.model()
        id_value = model._data[row][0]  # предполагается, что первый столбец — PK
        table_name = self.table_names[self.ui.comboBox_table.currentIndex()]
        reply = QMessageBox.question(
            self, "Удалить",
            f"Вы уверены, что хотите удалить запись с ID = {id_value} из таблицы {table_name}?",
            QMessageBox.Yes | QMessageBox.No
        )
        if reply == QMessageBox.Yes:
            try:
                with self.conn.cursor() as cur:
                    cur.execute(f'DELETE FROM "{table_name}" WHERE "{model._headers[0]}" = %s;', (id_value,))
                self.conn.commit()
                QMessageBox.information(self, "Удалить", "Запись успешно удалена.")
                self.load_table_data(self.ui.comboBox_table.currentIndex())
            except Exception as e:
                self.conn.rollback()
                QMessageBox.critical(self, "Ошибка", f"Ошибка при удалении записи:\n{e}")

    def get_table_headers(self, table_name):
        try:
            with self.conn.cursor() as cur:
                cur.execute(f'SELECT * FROM "{table_name}" LIMIT 0;')
                return [desc[0] for desc in cur.description]
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось получить заголовки таблицы:\n{e}")
            return []
