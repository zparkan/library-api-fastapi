from typing import Optional

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI(
    title="Library API",
    description="یک سیستم کتابداری ساده با FastAPI (بدون دیتابیس، داده‌ها در حافظه)",
    version="1.0.0",
)


# ---------- مدل‌ها (Schemas) ----------
class BookCreate(BaseModel):
    """داده‌ای که کاربر هنگام ساخت کتاب می‌فرستد."""
    title: str = Field(..., min_length=1, examples=["Clean Code"])
    author: str = Field(..., min_length=1, examples=["Robert C. Martin"])
    year: Optional[int] = Field(None, ge=0, le=2100, examples=[2008])


class BookUpdate(BaseModel):
    """برای PATCH: همه‌ی فیلدها اختیاری هستند."""
    title: Optional[str] = Field(None, min_length=1)
    author: Optional[str] = Field(None, min_length=1)
    year: Optional[int] = Field(None, ge=0, le=2100)


class Book(BookCreate):
    """کتاب کامل، همراه با id."""
    id: int


# ---------- "دیتابیس" در حافظه ----------
books_db: dict[int, Book] = {
    1: Book(id=1, title="Clean Code", author="Robert C. Martin", year=2008),
    2: Book(id=2, title="The Pragmatic Programmer", author="Andrew Hunt", year=1999),
}
next_id: int = 3


def get_book_or_404(book_id: int) -> Book:
    book = books_db.get(book_id)
    if book is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Book with id {book_id} not found",
        )
    return book


# ---------- Endpoints ----------
@app.get("/books", response_model=list[Book])
def list_books():
    """دریافت لیست همه‌ی کتاب‌ها."""
    return list(books_db.values())


@app.post("/books", response_model=Book, status_code=status.HTTP_201_CREATED)
def create_book(payload: BookCreate):
    """اضافه کردن کتاب جدید."""
    global next_id
    book = Book(id=next_id, **payload.model_dump())
    books_db[next_id] = book
    next_id += 1
    return book


@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    """گرفتن اطلاعات یک کتاب خاص."""
    return get_book_or_404(book_id)


@app.patch("/books/{book_id}", response_model=Book)
def update_book(book_id: int, payload: BookUpdate):
    """تغییر بخشی از اطلاعات یک کتاب (فقط فیلدهای ارسال‌شده عوض می‌شوند)."""
    book = get_book_or_404(book_id)
    changes = payload.model_dump(exclude_unset=True)
    updated = book.model_copy(update=changes)
    books_db[book_id] = updated
    return updated


@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int):
    """حذف یک کتاب."""
    get_book_or_404(book_id)
    del books_db[book_id]
