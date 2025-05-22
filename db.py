import psycopg2
from psycopg2 import OperationalError

def test_connection():
    try:
        conn = psycopg2.connect(
            dbname='postgres',
            user='postgres',
            password='databaseadmin',
            host='localhost',
            port='5432'
        )
        print("Подключение успешно!")
        cur = conn.cursor()
        cur.close()
        return conn
    except OperationalError as e:
        print("Ошибка подключения:", e)
        return None
