def get_all_tours_with_hotel_and_carrier(conn):
    query = """
    SELECT 
        т.id_тура,
        т.страна,
        т.город,
        т.продолжительность_дней,
        т.цена,
        о.название AS отель,
        п.название AS перевозчик
    FROM Туры т
    LEFT JOIN Отели о ON т.id_отеля = о.id_отеля
    LEFT JOIN Перевозчики п ON т.id_перевозчика = п.id_перевозчика;
    """
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()


def get_clients_with_purchase_count(conn):
    query = """
    SELECT 
        к.ФИО, 
        к.телефон, 
        к.количество_покупок
    FROM Клиенты к
    ORDER BY к.количество_покупок DESC;
    """
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()


def get_excursions_for_tours(conn):
    query = """
    SELECT 
        т.страна as страна_тура,
        т.город, 
        э.название as название_экскурсии, 
        э.тип, 
        э.продолжительность_часов, 
        э.описание, 
        э.цена
    FROM Экскурсии э
    JOIN Экскурсии_Туры эт ON э.id_экскурсии = эт.id_экскурсии
    JOIN Туры т on т.id_тура = эт.id_тура
    ORDER BY т.страна, т.город, э.тип;
    """
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()


def get_contracts_with_client_tour_employee(conn):
    query = """
    SELECT 
    д.id_договора, 
    кл.ФИО AS клиент, 
    т.страна, 
    т.город, 
    с.ФИО AS сотрудник, 
    д.дата_подписания, 
    CASE 
        WHEN д.статус_оплаты = true THEN 'Оплачено'
        ELSE 'Не оплачено'
    END AS статус_оплаты
    FROM Договоры_клиенты д
    JOIN Клиенты кл ON д.id_клиента = кл.id_клиента
    JOIN Туры т ON д.id_тура = т.id_тура
    JOIN Сотрудники с ON д.id_сотрудника = с.id_сотрудника;
    """
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()


def get_employees_with_positions_and_salaries(conn):
    query = """
    SELECT 
        с.ФИО, 
        д.название_должности, 
        д.оклад,
        с.дата_рождения,
        с.пол,
        с.телефон,
        с.паспорт,
        с.ИНН
    FROM Сотрудники с
    JOIN Должности д ON с.id_должности = д.id_должности
    ORDER BY с.ФИО, д.название_должности;
    """
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()


def get_hotel_contracts_with_employee(conn):
    query = """
    SELECT 
        до.id_договора,
        о.название as название_отеля,
        о.цена,
        до.дата_подписания,
        до.дата_окончания,
        с.ФИО as сотрудник
    FROM Договоры_партнёры_отели до
    JOIN Отели о on до.id_отеля = о.id_отеля
    JOIN Сотрудники с on до.id_сотрудника = с.id_сотрудника
    ORDER BY о.название;
    """
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()


def get_excursion_contracts_with_employee(conn):
    query = """
    SELECT 
        дэ.id_договора,
        э.название as название_экскурсии,
        э.цена,
        дэ.дата_подписания,
        дэ.дата_окончания,
        с.ФИО as сотрудник
    FROM Договоры_партнёры_экскурсии дэ
    JOIN Экскурсии э on дэ.id_экскурсии = э.id_экскурсии
    JOIN Сотрудники с on дэ.id_сотрудника = с.id_сотрудника
    ORDER BY э.название;
    """
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()


def get_carrier_contracts_with_employee(conn):
    query = """
    SELECT 
        дп.id_договора,
        п.название as перевозчик,
        п.цена,
        дп.дата_подписания,
        дп.дата_окончания,
        с.ФИО as сотрудник
    FROM Договоры_партнёры_перевозчики дп
    JOIN Перевозчики п on дп.id_перевозчика = п.id_перевозчика
    JOIN Сотрудники с on дп.id_сотрудника = с.id_сотрудника
    ORDER BY п.название;
    """
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()


def get_unpaid_contracts(conn):
    query = """
    SELECT 
        д.id_договора, 
        кл.ФИО AS клиент, 
        т.страна, 
        т.город, 
        д.дата_подписания
    FROM Договоры_клиенты д
    JOIN Клиенты кл ON д.id_клиента = кл.id_клиента
    JOIN Туры т ON д.id_тура = т.id_тура
    WHERE д.статус_оплаты = FALSE;
    """
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()


def get_tour_price_stats_by_country(conn):
    query = """
    SELECT 
        страна, 
        ROUND(AVG(цена)::numeric, 2) AS средняя_цена,
        MIN(цена) as минимальная_цена,
        MAX(цена) as максимальная_цена
    FROM Туры
    GROUP BY страна
    ORDER BY средняя_цена DESC;
    """
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()


def get_hotels_with_meals_and_capacity(conn):
    query = """
    SELECT 
        о.название, 
        о.страна, 
        о.город, 
        о.макс_вместимость_номера
    FROM Отели о
    WHERE о.питание = TRUE
    ORDER BY о.название, о.макс_вместимость_номера;
    """
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()


def get_contract_count_by_employee(conn):
    query = """
    SELECT 
        с.ФИО, 
        COUNT(д.id_договора) AS количество_договоров
    FROM Сотрудники с
    LEFT JOIN Договоры_клиенты д ON с.id_сотрудника = д.id_сотрудника
    GROUP BY с.ФИО
    ORDER BY количество_договоров DESC;
    """
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()


def get_clients_with_no_purchases(conn):
    query = """
    SELECT 
        к.ФИО, 
        к.телефон
    FROM Клиенты к
    WHERE к.количество_покупок = 0;
    """
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()


def get_tours_with_excursion_counts(conn):
    query = """
    SELECT 
        т.id_тура, 
        т.страна, 
        т.город, 
        COUNT(эт.id_экскурсии) AS количество_экскурсий
    FROM Туры т
    LEFT JOIN Экскурсии_Туры эт ON т.id_тура = эт.id_тура
    GROUP BY т.id_тура, т.страна, т.город
    ORDER BY количество_экскурсий DESC;
    """
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()


def get_total_revenue_per_tour(conn):
    query = """
    SELECT 
        т.id_тура,
        т.страна,
        т.город,
        т.цена AS цена_тура,
        п.цена AS цена_перевозчика,
        о.цена AS цена_отеля,
        COALESCE(SUM(э.цена), 0) AS сумма_экскурсий,
        (т.цена + п.цена + о.цена + COALESCE(SUM(э.цена), 0)) AS общая_выручка
    FROM Туры т
    LEFT JOIN Отели о ON т.id_отеля = о.id_отеля
    LEFT JOIN Перевозчики п ON т.id_перевозчика = п.id_перевозчика
    LEFT JOIN Экскурсии_Туры эт ON т.id_тура = эт.id_тура
    LEFT JOIN Экскурсии э ON эт.id_экскурсии = э.id_экскурсии
    GROUP BY т.id_тура, т.страна, т.город, т.цена, п.цена, о.цена
    ORDER BY общая_выручка DESC;
    """
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()
