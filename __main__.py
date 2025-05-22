import sys
from PySide6.QtWidgets import QApplication
from main_window import MainWindow
from db import test_connection
from triggers import create_date_check_triggers

def main():
    conn = test_connection()
    if conn:
        try:
            create_date_check_triggers(conn)
            print("Триггеры созданы или уже существуют.")
        except Exception as e:
            print("Ошибка при создании триггеров:", e)
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        sys.exit(app.exec())
        conn.close()
    else:
        print("Не удалось подключиться к базе.")

if __name__ == "__main__":
    main()
