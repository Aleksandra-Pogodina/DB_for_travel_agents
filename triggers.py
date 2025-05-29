def create_date_check_triggers(conn):
    sql = """
    SET search_path TO курсовая;

    CREATE OR REPLACE FUNCTION check_dates_order()
    RETURNS trigger AS $$
    BEGIN
        IF NEW.дата_окончания IS NOT NULL AND NEW.дата_подписания IS NOT NULL THEN
            IF NEW.дата_окончания <= NEW.дата_подписания THEN
                RAISE EXCEPTION 'Дата окончания (%) должна быть позже даты подписания (%)', NEW.дата_окончания, NEW.дата_подписания;
            END IF;
        END IF;
        RETURN NEW;
    END;
    $$ LANGUAGE plpgsql;

    DROP TRIGGER IF EXISTS trg_check_dates_dogovory_partnery_oteli ON "Договоры_партнёры_отели";
    CREATE TRIGGER trg_check_dates_dogovory_partnery_oteli
    BEFORE INSERT OR UPDATE ON "Договоры_партнёры_отели"
    FOR EACH ROW EXECUTE FUNCTION check_dates_order();

    DROP TRIGGER IF EXISTS trg_check_dates_dogovory_partnery_perevozchiki ON "Договоры_партнёры_перевозчики";
    CREATE TRIGGER trg_check_dates_dogovory_partnery_perevozchiki
    BEFORE INSERT OR UPDATE ON "Договоры_партнёры_перевозчики"
    FOR EACH ROW EXECUTE FUNCTION check_dates_order();

    DROP TRIGGER IF EXISTS trg_check_dates_dogovory_partnery_ekskursii ON "Договоры_партнёры_экскурсии";
    CREATE TRIGGER trg_check_dates_dogovory_partnery_ekskursii
    BEFORE INSERT OR UPDATE ON "Договоры_партнёры_экскурсии"
    FOR EACH ROW EXECUTE FUNCTION check_dates_order();
    
    
    ------------------------------------------------------------------------------

    CREATE OR REPLACE FUNCTION check_dates_payment()
    RETURNS trigger AS $$
    BEGIN
        -- Проверяем, что дата_оплаты больше даты_подписания, если дата_оплаты указана
        IF NEW.дата_оплаты IS NOT NULL AND NEW.дата_подписания IS NOT NULL THEN
            IF NEW.дата_оплаты <= NEW.дата_подписания THEN
                RAISE EXCEPTION 'Дата оплаты (%) должна быть позже даты подписания (%)', NEW.дата_оплаты, NEW.дата_подписания;
            END IF;
        END IF;
        RETURN NEW;
    END;
    $$ LANGUAGE plpgsql;
    
    DROP TRIGGER IF EXISTS trg_check_dates_dogovory_klienty ON "Договоры_клиенты";
    CREATE TRIGGER trg_check_dates_dogovory_klienty
    BEFORE INSERT OR UPDATE ON "Договоры_клиенты"
    FOR EACH ROW EXECUTE FUNCTION check_dates_payment();

    -----------------------------------------------------------------------------------------------------------
    CREATE OR REPLACE FUNCTION update_tour_price()
    RETURNS TRIGGER AS $$
    DECLARE
        hotel_price NUMERIC := 0;
        carrier_price NUMERIC := 0;
        excursions_sum NUMERIC := 0;
    BEGIN
        -- Получаем цену отеля
        IF NEW.id_отеля IS NOT NULL THEN
            SELECT цена INTO hotel_price FROM Отели WHERE id_отеля = NEW.id_отеля;
        END IF;
    
        -- Получаем цену перевозчика
        IF NEW.id_перевозчика IS NOT NULL THEN
            SELECT цена INTO carrier_price FROM Перевозчики WHERE id_перевозчика = NEW.id_перевозчика;
        END IF;
    
        -- Суммируем цены экскурсий, связанных с туром
        SELECT COALESCE(SUM(э.цена), 0) INTO excursions_sum
        FROM Экскурсии э
        JOIN Экскурсии_Туры эт ON э.id_экскурсии = эт.id_экскурсии
        WHERE эт.id_тура = NEW.id_тура;
    
        -- Вычисляем итоговую цену тура
        NEW.цена := hotel_price + carrier_price + excursions_sum;
    
        RETURN NEW;
    END;
    $$ LANGUAGE plpgsql;
    
    
    CREATE TRIGGER trg_update_tour_price
    BEFORE INSERT OR UPDATE ON Туры
    FOR EACH ROW
    EXECUTE FUNCTION update_tour_price();
    
    -------------------------------------------------------------------------------------------------------------
    
    
    CREATE OR REPLACE FUNCTION update_tour_price_on_hotel_change()
    RETURNS TRIGGER AS $$
    DECLARE
        carrier_price NUMERIC := 0;
        excursions_sum NUMERIC := 0;
    BEGIN
        -- Для каждого тура с изменённым отелем пересчитываем цену
        UPDATE Туры t
        SET цена = (NEW.цена + 
                    COALESCE((
                        SELECT цена FROM Перевозчики WHERE id_перевозчика = t.id_перевозчика
                    ), 0) + 
                    COALESCE((
                        SELECT SUM(э.цена)
                        FROM Экскурсии э
                        JOIN Экскурсии_Туры эт ON э.id_экскурсии = эт.id_экскурсии
                        WHERE эт.id_тура = t.id_тура
                    ), 0)) * COALESCE(t.продолжительность_дней, 1)
        WHERE t.id_отеля = NEW.id_отеля;
    
        RETURN NEW;
    END;
    $$ LANGUAGE plpgsql;
    
    CREATE TRIGGER trg_update_tour_price_on_hotel_change
    AFTER UPDATE OF цена ON Отели
    FOR EACH ROW
    EXECUTE FUNCTION update_tour_price_on_hotel_change();

    -----------------------------------------------------------------------------------------------------
    
    CREATE OR REPLACE FUNCTION update_tour_price_on_carrier_change()
    RETURNS TRIGGER AS $$
    BEGIN
        UPDATE Туры t
        SET цена = (
            COALESCE((
                SELECT цена FROM Отели WHERE id_отеля = t.id_отеля
            ), 0) +
            NEW.цена +
            COALESCE((
                SELECT SUM(э.цена)
                FROM Экскурсии э
                JOIN Экскурсии_Туры эт ON э.id_экскурсии = эт.id_экскурсии
                WHERE эт.id_тура = t.id_тура
            ), 0)
        ) * COALESCE(t.продолжительность_дней, 1)
        WHERE t.id_перевозчика = NEW.id_перевозчика;
    
        RETURN NEW;
    END;
    $$ LANGUAGE plpgsql;
    
    CREATE TRIGGER trg_update_tour_price_on_carrier_change
    AFTER UPDATE OF цена ON Перевозчики
    FOR EACH ROW
    EXECUTE FUNCTION update_tour_price_on_carrier_change();

------------------------------------------------------------------------------------------------------------------
    
    CREATE OR REPLACE FUNCTION update_tour_price_on_excursion_change()
    RETURNS TRIGGER AS $$
    DECLARE
        affected_tours RECORD;
    BEGIN
        FOR affected_tours IN
            SELECT DISTINCT эт.id_тура
            FROM Экскурсии_Туры эт
            WHERE эт.id_экскурсии = NEW.id_экскурсии
        LOOP
            UPDATE Туры t
            SET цена = (
                COALESCE((
                    SELECT цена FROM Отели WHERE id_отеля = t.id_отеля
                ), 0) +
                COALESCE((
                    SELECT цена FROM Перевозчики WHERE id_перевозчика = t.id_перевозчика
                ), 0) +
                COALESCE((
                    SELECT SUM(э2.цена)
                    FROM Экскурсии э2
                    JOIN Экскурсии_Туры эт2 ON э2.id_экскурсии = эт2.id_экскурсии
                    WHERE эт2.id_тура = t.id_тура
                ), 0)
            ) * COALESCE(t.продолжительность_дней, 1)
            WHERE t.id_тура = affected_tours.id_тура;
        END LOOP;
    
        RETURN NEW;
    END;
    $$ LANGUAGE plpgsql;
    
    CREATE TRIGGER trg_update_tour_price_on_excursion_change
    AFTER UPDATE OF цена ON Экскурсии
    FOR EACH ROW
    EXECUTE FUNCTION update_tour_price_on_excursion_change();

    
    """

    with conn.cursor() as cur:
        cur.execute(sql)
    conn.commit()
