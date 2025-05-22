from PySide6.QtWidgets import QDialog, QMessageBox, QLineEdit, QFormLayout
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

        # Создаём поля для каждого столбца, кроме первичного ключа (предполагается, что это первый столбец)
        for i, header in enumerate(headers):
            if i == 0:
                # Не показываем поле для первичного ключа (id)
                continue
            line_edit = QLineEdit(self)
            if record:
                value = str(record[i]) if record[i] is not None else ""
                line_edit.setText(value)
            self.ui.formLayout_dialog.addRow(header, line_edit)
            self.fields[header] = line_edit

        self.ui.btn_save.clicked.connect(self.save_data)
        self.ui.btn_cancel.clicked.connect(self.reject)

    def save_data(self):
        try:
            with self.conn.cursor() as cur:
                if self.record:
                    # Обновление
                    set_clause = ", ".join([f'"{h}" = %s' for h in self.fields.keys()])
                    query = f'UPDATE "{self.table_name}" SET {set_clause} WHERE "{self.headers[0]}" = %s'
                    values = [self.fields[h].text() for h in self.fields] + [self.record[0]]
                    cur.execute(query, values)
                else:
                    # Добавление
                    columns = ", ".join([f'"{h}"' for h in self.fields.keys()])
                    placeholders = ", ".join(["%s"] * len(self.fields))
                    query = f'INSERT INTO "{self.table_name}" ({columns}) VALUES ({placeholders})'
                    values = [self.fields[h].text() for h in self.fields]
                    cur.execute(query, values)
                self.conn.commit()
            self.accept()
        except Exception as e:
            self.conn.rollback()
            QMessageBox.critical(self, "Ошибка", f"Ошибка при сохранении данных:\n{e}")
