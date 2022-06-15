## CRUD Restaurants built with Django Rest Framework, React & Docker

Components:
* Web Framework [Django Rest Framework](https://www.django-rest-framework.org/)
* React [Celery](https://reactjs.org/)
* Database [PostgreSQL](https://www.postgresql.org)

### Install

---

Types of installation

1. [Docker-compose](#docker-compose-install)

#### Docker-compose install

Uses the default Django development server.

1. Rename *.env.example* to *.env*.
2. Update the environment variables in the *.env* file.
3. Prepare Django environment to start up

```bash
$ cd backend
$ python3.9 -m venv .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py createsuperuser
$ python manage.py collectstatic
```

4. Build the images and run the containers:

```bash
$ docker-compose up --build
```