# FastAPI PostgreSQL Project

Проект на FastAPI с PostgreSQL базой данных для управления задачами.

## Технологии

- FastAPI
- PostgreSQL
- SQLAlchemy
- Alembic
- Pydantic

## Установка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/your-username/fastapi-postgresql.git
cd fastapi-postgresql
```

2. Создайте виртуальное окружение:
```bash
python -m venv venv
source venv/bin/activate  # для Linux/Mac
venv\Scripts\activate     # для Windows
```

3. Установите зависимости:
```bash
pip install -r requirements.txt
```

4. Создайте файл .env в корневой директории:
```
PG_HOST=localhost
PG_USER=postgres
PG_PASS=postgres
PG_DB=fastapi_db
```

5. Примените миграции:
```bash
alembic upgrade head
```

6. Запустите сервер:
```bash
uvicorn app.main:app --reload
```

## API Endpoints

- `GET /api/v1/tasks` - получить список задач
- `POST /api/v1/tasks` - создать новую задачу
- `GET /api/v1/tasks/{task_id}` - получить задачу по ID
- `PUT /api/v1/tasks/{task_id}` - обновить задачу
- `PATCH /api/v1/tasks/{task_id}/status` - изменить статус задачи
- `DELETE /api/v1/tasks/{task_id}` - удалить задачу

## Документация API

После запуска сервера документация доступна по адресам:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc 