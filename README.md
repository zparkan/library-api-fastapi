# 📚 Library API (FastAPI)

🇮🇷 [نسخه فارسی (Persian version)](#-راهنمای-فارسی)

A simple library management REST API built with **FastAPI**.
There is no database: all data is stored in memory (a Python dictionary), so it resets every time the server restarts.

## Features

- List all books
- Add a new book
- Get a single book by id
- Partially update a book (PATCH)
- Delete a book
- Automatic interactive docs (Swagger UI)
- Input validation with Pydantic and proper 404 errors

## Tech stack

- Python 3.9+
- FastAPI
- Uvicorn

## Installation

```bash
git clone https://github.com/zparkan/library-api-fastapi.git
cd library-api-fastapi

python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

pip install -r requirements.txt
```

## Run

```bash
uvicorn main:app --reload
```

- API: http://127.0.0.1:8000
- Swagger docs: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## Endpoints

| Method | Path          | Description            | Success code |
|--------|---------------|------------------------|--------------|
| GET    | `/books`      | List all books         | 200          |
| POST   | `/books`      | Add a new book         | 201          |
| GET    | `/books/{id}` | Get one book           | 200          |
| PATCH  | `/books/{id}` | Update a book partially| 200          |
| DELETE | `/books/{id}` | Delete a book          | 204          |

If the book does not exist, the API returns `404 Not Found`.

## Book model

```json
{
  "id": 1,
  "title": "Clean Code",
  "author": "Robert C. Martin",
  "year": 2008
}
```

`title` and `author` are required when creating; `year` is optional.

## Examples (curl)

```bash
# List books
curl http://127.0.0.1:8000/books

# Add a book
curl -X POST http://127.0.0.1:8000/books \
  -H "Content-Type: application/json" \
  -d '{"title": "Refactoring", "author": "Martin Fowler", "year": 1999}'

# Get one book
curl http://127.0.0.1:8000/books/1

# Update only the year
curl -X PATCH http://127.0.0.1:8000/books/1 \
  -H "Content-Type: application/json" \
  -d '{"year": 2009}'

# Delete a book
curl -X DELETE http://127.0.0.1:8000/books/1
```

## Project structure

```
library-api-fastapi/
├── main.py
├── requirements.txt
└── README.md
```

## Notes

Data lives in memory only. For persistence, a database (e.g. SQLite + SQLAlchemy) can be added later.


---

## 🇮🇷 راهنمای فارسی

<div dir="rtl">

### 📚 API کتابداری (FastAPI)

یک API ساده برای مدیریت کتابخانه که با **FastAPI** ساخته شده است.
دیتابیس ندارد و تمام داده‌ها در حافظه (یک دیکشنری پایتون) نگهداری می‌شوند؛ بنابراین با هر بار راه‌اندازی مجدد سرور، داده‌ها به حالت اولیه برمی‌گردند.

#### امکانات

- دریافت لیست همه‌ی کتاب‌ها
- افزودن کتاب جدید
- دریافت اطلاعات یک کتاب با id
- ویرایش جزئی کتاب (PATCH)
- حذف کتاب
- مستندات تعاملی خودکار (Swagger UI)
- اعتبارسنجی ورودی با Pydantic و پاسخ 404 مناسب

#### تکنولوژی‌ها

- پایتون نسخه ۳.۹ به بالا
- FastAPI
- Uvicorn

#### نصب

</div>

```bash
git clone https://github.com/zparkan/library-api-fastapi.git
cd library-api-fastapi

python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

pip install -r requirements.txt
```

<div dir="rtl">

#### اجرا

</div>

```bash
uvicorn main:app --reload
```

<div dir="rtl">

- خود API: http://127.0.0.1:8000
- مستندات Swagger: http://127.0.0.1:8000/docs
- مستندات ReDoc: http://127.0.0.1:8000/redoc

#### Endpointها

| متد | مسیر | توضیح | کد موفقیت |
|-----|------|-------|-----------|
| GET | `/books` | دریافت لیست کتاب‌ها | 200 |
| POST | `/books` | افزودن کتاب جدید | 201 |
| GET | `/books/{id}` | دریافت یک کتاب | 200 |
| PATCH | `/books/{id}` | ویرایش جزئی کتاب | 200 |
| DELETE | `/books/{id}` | حذف کتاب | 204 |

اگر کتاب موجود نباشد، API خطای `404 Not Found` برمی‌گرداند.

#### مدل کتاب

فیلدهای `title` و `author` هنگام ساخت کتاب اجباری‌اند و `year` اختیاری است.

</div>

```json
{
  "id": 1,
  "title": "Clean Code",
  "author": "Robert C. Martin",
  "year": 2008
}
```

<div dir="rtl">

#### نمونه دستورها (curl)

نمونه‌ی دستورها در بخش انگلیسی بالا (Examples) آمده است: لیست کتاب‌ها، افزودن، دریافت، ویرایش سال و حذف.

#### ساختار پروژه

</div>

```
library-api-fastapi/
├── main.py            # کد اصلی برنامه
├── requirements.txt   # کتابخانه‌های مورد نیاز
└── README.md          # راهنما
```

<div dir="rtl">

#### نکته

داده‌ها فقط در حافظه هستند. برای ماندگاری داده‌ها می‌توان بعداً یک دیتابیس (مثلاً SQLite + SQLAlchemy) اضافه کرد.

</div>
