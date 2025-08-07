# Проект на Django REST API

## Инструкция по запуску

1. Клонируйте репозиторий:
git clone <ссылка_на_репозиторий>

markdown
Копировать
Редактировать

2. Перейдите в директорию проекта:
cd <название_папки_с_проектом>

r
Копировать
Редактировать

3. Создайте и активируйте виртуальное окружение:
- Для Windows:
  ```
  python -m venv .venv
  .\.venv\Scripts\activate
  ```
- Для MacOS/Linux:
  ```
  python3 -m venv .venv
  source .venv/bin/activate
  ```

4. Установите зависимости:
pip install -r requirements.txt

markdown
Копировать
Редактировать

5. Скопируйте файл `.env.example` в `.env`:
cp .env.example .env

markdown
Копировать
Редактировать

6. Откройте файл `.env` и добавьте свои данные, такие как параметры базы данных, секретные ключи и другие переменные среды.

Пример конфигурации `.env`:
SECRET_KEY=your_secret_key
DEBUG=True
DATABASE_URL=postgres://postgres:password@localhost:5432/your_db_name
JWT_SECRET_KEY=your_jwt_secret_key

markdown
Копировать
Редактировать

7. Выполните миграции базы данных:
python manage.py migrate

markdown
Копировать
Редактировать

8. Запустите сервер:
python manage.py runserver

markdown
Копировать
Редактировать

## Технологии

- **Django REST Framework (DRF)** - для создания API.
- **DRF Spectacular** - для генерации и документации API (Swagger).
- **JWT Authentication** - для аутентификации пользователей.
- **Psycopg2** - для работы с PostgreSQL.

## API Endpoints

**1. Регистрация пользователя**
- **URL**: `/register`
- **Метод**: `POST`
- **Тело запроса**:
```json
{
 "username": "example_user",
 "email": "user@example.com",
 "password": "yourpassword"
}
Ответ:

json
Копировать
Редактировать
{
  "message": "User created successfully"
}
2. Логин пользователя

URL: /login

Метод: POST

Тело запроса:

json
Копировать
Редактировать
{
  "username": "example_user",
  "password": "yourpassword"
}
Ответ:

json
Копировать
Редактировать
{
  "token": "your_jwt_token"
}
3. Получение списка событий

URL: /events-list

Метод: GET

Требуется аутентификация: Да (JWT Token в заголовке Authorization)

Ответ:

json
Копировать
Редактировать
[
  {
    "id": 1,
    "title": "Event Title",
    "description": "Event Description",
    "date": "2025-08-07T15:00:00",
    "location": "Location",
    "organizer": "Organizer Name"
  }
]
4. Создание события

URL: /events

Метод: POST

Тело запроса:

json
Копировать
Редактировать
{
  "title": "Event Title",
  "description": "Event Description",
  "date": "2025-08-07T15:00:00",
  "location": "Location"
}
Ответ:

json
Копировать
Редактировать
{
  "message": "Event created successfully"
}