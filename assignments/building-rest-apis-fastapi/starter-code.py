from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI(title="Library API")


class Book(BaseModel):
    # TODO: Add the fields: id, title, author, and publication_year
    pass


class BookCreate(BaseModel):
    # TODO: Add title, author, and publication_year fields with validation
    pass


# TODO: Initialize a list of sample books
books = []


@app.get("/books")
def get_books():
    # TODO: Return all books
    pass


@app.get("/books/{book_id}")
def get_book(book_id: int):
    # TODO: Find and return the requested book
    pass


@app.post("/books", status_code=status.HTTP_201_CREATED)
def create_book(book_data: BookCreate):
    # TODO: Create a new Book with a unique ID and add it to the list
    pass


@app.put("/books/{book_id}")
def update_book(book_id: int, book_data: BookCreate):
    # TODO: Update the matching book or raise HTTP 404
    pass


@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    # TODO: Remove the matching book or raise HTTP 404
    pass
