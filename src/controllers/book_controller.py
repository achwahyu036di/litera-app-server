from fastapi import APIRouter, File, HTTPException, Depends, UploadFile
from sqlalchemy.orm import Session
from ..models.book import Book
from ..schemas.book_schema import BookSchema
from ..db.database import get_db
from ..utils.response_wrapper import api_response
from ..utils.cloudinary_uploader import upload_image

route = APIRouter()


# Creat Book
@route.post("/book/")
def creat_book(book: BookSchema, db: Session = Depends(get_db)):
    # add new book
    now_book = Book(**book.dict())
    db.add(now_book)
    db.commit()
    db.refresh(now_book)
    return api_response(
        data=now_book,
        message="Book already registerd"
    )

# Read book bay id
@route.get("/book/{book_id}")
def get_book(book_id: str, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()
    return api_response(
        data=book,
        message="Book retriveed successfully"
    )

# Update book
@route.put("/book/{book_id}")
def updata_book(book_id: str, user_update: BookSchema, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()
    if book is None:
        raise HTTPException(status_code=404, detail="Book not Found")
    for field, value in user_update.dict(exclude_unset=True).items():
        setattr(book, field, value)
    
    db.commit()
    db.refresh(book)
    return api_response(
        data=book,
        message=" customer updated successfully"
    )

# Delete Book
@route.delete("/book/{book_id}")
def delete_book(book_id: str,  db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    db.delete(book)
    db.commit()
    return api_response(
        message="Book deleted successfully"
    )

# upload book image
@route.post("/book/{book_id}/cover")
def update_cover_image(
    book_id: str,
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    # Upload ke folder 'book_covers' di Cloudinary
    image_url = upload_image(file, "project_peminjaman_buku/book_covers")
    
    book.cover_image_url = image_url
    db.commit()
    db.refresh(book)
    return book