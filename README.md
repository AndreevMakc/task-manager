# FastAPI PostgreSQL Project

Проект на FastAPI с использованием PostgreSQL и SQLAlchemy.

## Установка

1. Создайте виртуальное окружение:
```bash
python -m venv venv
source venv/bin/activate  # для Linux/Mac
venv\Scripts\activate     # для Windows
```

2. Установите зависимости:
```bash
pip install -r requirements.txt
```

3. Создайте файл .env в корневой директории проекта:
```
DATABASE_URL=postgresql://user:password@localhost:5432/dbname
```

4. Примените миграции:
```bash
alembic upgrade head
```

5. Запустите сервер:
```bash
uvicorn app.main:app --reload
```

## Структура проекта

```
├── alembic/              # Миграции базы данных
├── app/
│   ├── api/             # API endpoints
│   ├── core/            # Конфигурация и настройки
│   ├── db/              # Работа с базой данных
│   ├── models/          # SQLAlchemy модели
│   └── schemas/         # Pydantic схемы
├── tests/               # Тесты
├── .env                 # Переменные окружения
├── alembic.ini          # Конфигурация Alembic
└── requirements.txt     # Зависимости проекта
``` 