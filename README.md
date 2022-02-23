# Bookstore API REST using Postgres Database

## Introduction

This is a simple API REST made with **django** and **django-rest-framework**. It uses **postgres** as database through **psycopg2**. We have to main entities: *books* and *authors*, in which every book is written by a single author and every author can write several books (*one-to-many*).

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

### Database config

Connection between django api and database is store in `bookstore_project.settings.py` file:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'bookstore',
        'USER': 'geronimo',
        'PASSWORD': '1234',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

This config is default config. Change as many fields as you need.

## Endpoints

There are endpoints to CRUD operations both authors and books.

### Authors

- **POST** `/api/authors`: create an author.
    ```json
    {
        "name": "Mark Twain",
        "added_by": "1"
    }
    ```

- **GET** `/api/authors`: list all authors currently available.
- **GET** `/api/authors/id`: return details of specified author.
- **PUT** `/api/authors/id`: update a author (all fields are optional).
    ```json
        {
            "name": "Mark Twain",
            "added_by": "1"
        }
    ```

- **DELETE** `/api/authors/id`: delete a author from database.

### Books

- **POST** `/api/books`: create a new book.
    ```json
    {
        "title": "Sarajevo",
        "description": "En nuestro ... tanto al",
        "added_by": "1",
        "author": "3"
    }
    ```

- **GET** `/api/books`: list all books currently available.
- **GET** `/api/books/id`: return book details.
- **PUT** `/api/books/id`: update a book (all fields are optional).
    ```json
    {
        "title": "Sarajevo",
        "description": "En nuestro ... tanto al",
        "added_by": "1",
        "author": "3"
    }
    ```

- **DELETE** `/api/books/id`: delete a book from database.

## Tools

- Django 4.0.2
- djangorestframework 3.13.1
- psycopg2
- Postgres