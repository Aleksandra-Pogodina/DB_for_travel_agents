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

    DROP TRIGGER IF EXISTS trg_check_dates_dogovory_klienty ON "Договоры_клиенты";
    CREATE TRIGGER trg_check_dates_dogovory_klienty
    BEFORE INSERT OR UPDATE ON "Договоры_клиенты"
    FOR EACH ROW EXECUTE FUNCTION check_dates_order();

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
    """

    with conn.cursor() as cur:
        cur.execute(sql)
    conn.commit()
