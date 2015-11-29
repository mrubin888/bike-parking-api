# bike-parking-api
A Django REST API for a bike parking app.

## Setup (Ubuntu 12.04)
1. Run `sudo apt-get update`.
2. Install postgres with `sudo apt-get install postgresql`.
3. Switch to postgres user.
4. Start postgres with `psql`.
5. Create a new database with `CREATE DATABASE dbname;`.
6. Create a new superuser with `CREATE ROLE username PASSWORD password SUPERUSER LOGIN;`.
7. Switch back to your project user.
8. Make sure you have python installed (tested on python 2.7). Install python with `sudo apt-get install python` if you need to.
9. Install utility packages libpq-dev and psycopg2 with `sudo apt-get install libpq-dev psycopg2`.
10. Install git with `sudo apt-get install git`.
11. Clone this repository with the `git clone` command.
12. Change directory into the root of the repository.
13. Install virtualenv with `sudo apt-get install python-virtualenv`.
14. Create a virtualenv with `virtualenv env`.
15. Activate the virtualenv you created with `source env/bin/activate`
16. Install Django with `pip install django`.
17. Install Django-Rest-Framework with `pip install djangorestframework`.
18. Install Psycopg2 with `pip install psycopg2`.
19. Update secret key and db info in `sample_settings.py` and save as `settings.py`.
20. Migrate your database with `python manage.py migrate`.
21. Create a superuser for your api with `python manage.py createsuperuser`.

## Testing
Run `python manage.py test`.

## Run Server
Run `python manage.py runserver 0.0.0.0:portno`.