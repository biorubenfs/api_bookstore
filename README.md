# Bookstore API REST using Postgres Database

## Introduction

This is a simple API REST made with **django** and **django-rest-framework**. It uses **postgres** as database through **psycopg2**. It

## Setup

All modules are in in `requirements.txt` file, so once you have downloaded the repo, simple run:

```bash
pip install -r requirements.txt
```

### Admin user
A default admin user was created with username *admin* and password *Palabra123$*

After that, run:

```bash
python manage.py makemigrations
```

and:
```bash
python manage.py migrate
```

And finally, you can start the server with:

```bash
python manage.py runserver
```

## Endpoints

There are endpoints to CRUD operations both authors and books.

### Authors

- **POST** `/api/authors`: create an author.
- **GET** `/api/authors`: list all authors currently available.
- **GET** `/api/authors/id`: return details of specified author.
- **PUT** `/api/authors/id`: update a author
- **DELETE** `/api/authors/id`: delete a author from database.

### Books

- **POST** `/api/books`: create a new book.
- **GET** `/api/books`: list all books currently available.
- **GET** `/api/books/id`: return book details.
- **PUT** `/api/books/id`: update a book
- **DELETE** `/api/books/id`: delete a book from database.

## Tools

- Django 4.0.2
- djangorestframework 3.13.1
- psycopg2
- Postgres