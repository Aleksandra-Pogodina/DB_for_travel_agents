-- Таблица должности
CREATE TABLE Должности (
    id_должности SERIAL PRIMARY KEY,
    название_должности VARCHAR(255) NOT NULL,
    оклад DECIMAL(10, 2) NOT NULL
);

-- Таблица сотрудники
CREATE TABLE Сотрудники (
    id_сотрудника SERIAL PRIMARY KEY,
    ФИО VARCHAR(255) NOT NULL,
    дата_рождения DATE NOT NULL,
    пол CHAR(1) CHECK (пол IN ('М', 'Ж')),
    телефон VARCHAR(20),
    паспорт VARCHAR(50),
    ИНН VARCHAR(50),
    id_должности INT NOT NULL,
    CONSTRAINT сотрудники_id_должности_fkey FOREIGN KEY (id_должности)
        REFERENCES Должности(id_должности) ON DELETE CASCADE
);

-- Таблица клиенты
CREATE TABLE Клиенты (
    id_клиента SERIAL PRIMARY KEY,
    ФИО VARCHAR(255) NOT NULL,
    телефон VARCHAR(20),
    количество_покупок INT DEFAULT 0
);

-- Таблица отели
CREATE TABLE Отели (
    id_отеля SERIAL PRIMARY KEY,
    название VARCHAR(255) NOT NULL,
    страна VARCHAR(255) NOT NULL,
    город VARCHAR(255) NOT NULL,
    адрес TEXT NOT NULL,
    питание BOOLEAN DEFAULT FALSE,
    макс_вместимость_номера INT NOT NULL,
    цена DECIMAL(10, 2) NOT NULL
);

-- Таблица перевозчики
CREATE TABLE Перевозчики (
    id_перевозчика SERIAL PRIMARY KEY,
    название VARCHAR(255) NOT NULL,
    тип VARCHAR(50) NOT NULL,
    цена DECIMAL(10, 2) NOT NULL
);

-- Таблица экскурсии
CREATE TABLE Экскурсии (
    id_экскурсии SERIAL PRIMARY KEY,
    название VARCHAR(255) NOT NULL,
    тип VARCHAR(255) NOT NULL,
    продолжительность_часов INT NOT NULL,
    описание TEXT,
    цена DECIMAL(10, 2) NOT NULL
);

-- Таблица туры
CREATE TABLE Туры (
    id_тура SERIAL PRIMARY KEY,
    страна VARCHAR(255) NOT NULL,
    город VARCHAR(255) NOT NULL,
    продолжительность_дней INT NOT NULL,
    цена DECIMAL(10, 2) NOT NULL,
    id_перевозчика INT,
    id_отеля INT,
    CONSTRAINT туры_id_перевозчика_fkey FOREIGN KEY (id_перевозчика)
        REFERENCES Перевозчики(id_перевозчика) ON DELETE CASCADE,
    CONSTRAINT туры_id_отеля_fkey FOREIGN KEY (id_отеля)
        REFERENCES Отели(id_отеля) ON DELETE CASCADE
);

-- Таблица экскурсии-тур
CREATE TABLE Экскурсии_Туры (
    id_тура INT NOT NULL,
    id_экскурсии INT NOT NULL,
    PRIMARY KEY (id_тура, id_экскурсии),
    CONSTRAINT экскурсии_туры_id_тура_fkey FOREIGN KEY (id_тура)
        REFERENCES Туры(id_тура) ON DELETE CASCADE,
    CONSTRAINT экскурсии_туры_id_экскурсии_fkey FOREIGN KEY (id_экскурсии)
        REFERENCES Экскурсии(id_экскурсии) ON DELETE CASCADE
);

-- Таблица договоры клиенты
CREATE TABLE Договоры_клиенты (
    id_договора SERIAL PRIMARY KEY,
    id_клиента INT NOT NULL,
    id_тура INT NOT NULL,
    id_сотрудника INT NOT NULL,
    дата_подписания DATE NOT NULL,
    дата_оплаты DATE DEFAULT NULL,
    статус_оплаты BOOLEAN DEFAULT FALSE,
    CONSTRAINT договоры_клиенты_id_клиента_fkey FOREIGN KEY (id_клиента)
        REFERENCES Клиенты(id_клиента) ON DELETE CASCADE,
    CONSTRAINT договоры_клиенты_id_тура_fkey FOREIGN KEY (id_тура)
        REFERENCES Туры(id_тура) ON DELETE CASCADE,
    CONSTRAINT договоры_клиенты_id_сотрудника_fkey FOREIGN KEY (id_сотрудника)
        REFERENCES Сотрудники(id_сотрудника) ON DELETE CASCADE
);

-- Таблица договоры_партнёры_отели
CREATE TABLE Договоры_партнёры_отели (
    id_договора SERIAL PRIMARY KEY,
    id_отеля INT NOT NULL,
    дата_подписания DATE NOT NULL,
    дата_окончания DATE NOT NULL,
    id_сотрудника INT NOT NULL,
    CONSTRAINT договоры_партнёры_отели_id_отеля_fkey FOREIGN KEY (id_отеля)
        REFERENCES Отели(id_отеля) ON DELETE CASCADE,
    CONSTRAINT договоры_партнёры_отели_id_сотрудника_fkey FOREIGN KEY (id_сотрудника)
        REFERENCES Сотрудники(id_сотрудника) ON DELETE CASCADE
);

-- Таблица договоры_партнёры_перевозчики
CREATE TABLE Договоры_партнёры_перевозчики (
    id_договора SERIAL PRIMARY KEY,
    id_перевозчика INT NOT NULL,
    дата_подписания DATE NOT NULL,
    дата_окончания DATE NOT NULL,
    id_сотрудника INT NOT NULL,
    CONSTRAINT договоры_партнёры_перевозчики_id_перевозчика_fkey FOREIGN KEY (id_перевозчика)
        REFERENCES Перевозчики(id_перевозчика) ON DELETE CASCADE,
    CONSTRAINT договоры_партнёры_перевозчики_id_сотрудника_fkey FOREIGN KEY (id_сотрудника)
        REFERENCES Сотрудники(id_сотрудника) ON DELETE CASCADE
);

-- Таблица договоры_партнёры_экскурсии
CREATE TABLE Договоры_партнёры_экскурсии (
    id_договора SERIAL PRIMARY KEY,
    id_экскурсии INT NOT NULL,
    дата_подписания DATE NOT NULL,
    дата_окончания DATE NOT NULL,
    id_сотрудника INT NOT NULL,
    CONSTRAINT договоры_партнёры_экскурсии_id_экскурсии_fkey FOREIGN KEY (id_экскурсии)
        REFERENCES Экскурсии(id_экскурсии) ON DELETE CASCADE,
    CONSTRAINT договоры_партнёры_экскурсии_id_сотрудника_fkey FOREIGN KEY (id_сотрудника)
        REFERENCES Сотрудники(id_сотрудника) ON DELETE CASCADE
);




----------------------
ALTER TABLE Договоры_клиенты
ADD CONSTRAINT check_payment_status
CHECK (дата_оплаты IS NULL OR статус_оплаты = TRUE);



ALTER TABLE "Туры" ALTER COLUMN "цена" DROP NOT NULL;









