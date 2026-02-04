Star Wars API

frameworks:  django, django restframework. database: postgresql

# Endpoints

* People: http://localhost:8000/api/people/ http methods: get
* People By ID:  http://localhost:8000/api/people/id/
* Films: http://localhost:8000/api/films/ http methods: get
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