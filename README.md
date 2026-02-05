Star Wars API

frameworks:  django, django restframework. database: postgresql

# Endpoints

* Register http://127.0.0.1:8000/api/auth/register/ http methods: post with username and password
* Loging http://127.0.0.1:8000/api/auth/login/ http methods: post with username, password and token
* Logout http://127.0.0.1:8000/api/auth/logout/ http methods: post with username and password and token
* People: http://localhost:8000/api/people/ http methods: get
* People By ID:  http://localhost:8000/api/people/id/
* Search people http://127.0.0.1:8000/api/people/?blond
* Ordering people http://127.0.0.1:8000/api/people/?ordering=name
* Films: http://localhost:8000/api/films/ http methods: get
* Search people ex http://127.0.0.1:8000/api/films/?6 
* Films By ID:  http://localhost:8000/api/films/id/
* Planets:  http://localhost:8000/api/planets/ http methods: get
* Planets By ID:  http://localhost:8000/api/planets/id/
* Starships:  http://localhost:8000/api/starships/ http methods: get
*  Starships By ID:  http://localhost:8000/api/starships/id/
* Vehicles:  http://localhost:8000/api/vehicles/
* Vehicles By ID:  http://localhost:8000/api/vehicles/id/

is necessary create an .env file with django secret key and database name, user, password, and host


commands:

initialize the uv 
```
 uv init
```

 start the django server
```
  uv run --env-file .env python manage.py runserver
```

 to create database migration
```
  uv run --env-file .env python manage.py  makemigrations
```

applying  the migration
```
 uv run --env-file .env python manage.py  migrate
```
to populate the api with star wars data
```
 uv run --env-file .env  python manage.py starwars_data 
```

tests
```
 uv run --env-file .env  python manage.py pytest
```