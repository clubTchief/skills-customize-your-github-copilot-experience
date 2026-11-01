# Building REST APIs with FastAPI

## Objective

Build a small REST API for managing a collection of books using FastAPI. You will practice defining routes, validating request data, using HTTP status codes, and testing API endpoints through automatic interactive documentation.

## Tasks

### Set Up the FastAPI Application

#### Description

Create a FastAPI application and define an in-memory collection of books. Use starter-code.py as a starting point.

#### Requirements

Completed program should:

- Create a FastAPI application named `app`
- Define a Pydantic model for a book with an ID, title, author, and publication year
- Initialize a list that stores sample books
- Start successfully with Uvicorn
- Display the automatic API documentation at `/docs`

### Implement Read Endpoints

#### Description

Add endpoints that let a client retrieve all books or one book by its ID.

#### Requirements

Completed program should:

- Return all books from `GET /books`
- Return one book from `GET /books/{book_id}`
- Return HTTP 404 with a clear message when the ID does not exist

### Implement Create and Update Endpoints

#### Description

Add endpoints for adding a new book and updating an existing book.

#### Requirements

Completed program should:

- Add a book with `POST /books` and return HTTP 201
- Generate a unique ID for each new book
- Validate that the title and author are not empty
- Reject publication years earlier than 1000
- Update an existing book with `PUT /books/{book_id}`
- Return HTTP 404 when an update targets an ID that does not exist

### Implement Delete and Error Handling

#### Description

Finish the API by allowing clients to delete books and by testing predictable error responses.

#### Requirements

Completed program should:

- Delete a book with `DELETE /books/{book_id}`
- Return HTTP 404 when a delete targets an ID that does not exist
- Return useful response messages for successful operations
- Test the API using `/docs`, including at least one successful and one unsuccessful request

## Setup

Install the required packages:

```bash
pip install -r requirements.txt
```

Start the API:

```bash
uvicorn starter-code:app --reload
```

Then open `http://127.0.0.1:8000/docs`.
