# FastAPI Product Management API

This is a FastAPI-based RESTful service that manages product data using a MySQL backend. It supports adding, updating, listing, and retrieving product information with enum validation, Pydantic schemas, and SQLAlchemy ORM.

---

## Features

-  Add a new product
-  Update an existing product
-  View product details by ID
-  Paginated product listing (10 per page)
-  API docs with Swagger UI
-  MySQL as the backend database
-  ORM using SQLAlchemy
-  Data validation using Pydantic

---

## Tech Stack

- Python 3.11+
- FastAPI
- SQLAlchemy
- Pydantic
- MySQL
- Uvicorn (for development server)

---

## Project Structure

.
├── main.py
├── models.py
├── schemas.py
├── crud.py
├── database.py
└── requirements.txt


---

## 🔧 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/ShindeKomal25/vibeosys-assesment-python-fastapi.git
cd vibeosys-assesment-python-fastapi

3. Install dependencies
pip install -r requirements.txt

4. Set up MySQL

Make sure MySQL is running and create a database:

CREATE DATABASE productdb;
Add your db creds in .env file

Running the Server
uvicorn main:app --reload

Open your browser and navigate to:

Swagger UI: http://127.0.0.1:8000/docs


