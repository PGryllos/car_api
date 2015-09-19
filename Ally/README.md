###Installation Guide

In order to run the api you need to have `Python2.7+`, `GeoDjango` with `PostgreSQL` and `PostGIS` extension installed.

Details
---

If you already have `Python` installed then 
* install `PostgreSQL` and `PostGIS`. You can either build from source or use your package manager. I installed version 9.4 for both using apt-get in Ubuntu 15.04 and it seems fine.

If something goes wrong have a look at the installation guide from [GeoDjango documentation](https://docs.djangoproject.com/en/1.8/ref/contrib/gis/install/postgis/)

After that, you can
* create a virtual environment and use `https://github.com/PGryllos/car_api.git` to clone the repository inside the virtual envrinonment directory. Activate virtual environment and run `pip install -r requirements.txt` to install the latest stable version of `Django` and `psycopg2`.

Then you need to 
* create a database. Run `sudo -u postgres createdb <DB_NAME>`. You will also need to create the PostGIS extension and a priviledged user for the data base. Run `sudo su - postgres` and then connect to the data base with `psql -d <DB_NAME>` and use `CREATE USER <username> WITH SUPERUSER PASSWORD <password>;` to create the user and `CREATE EXTENSION postgis;` to enable spatial functionality.

Use \<DB_NAME\> = 'CarsDB', \<username\> = 'testuser' and \<password\> = 'test'. If you use different values you will also have to make the same changes in the manage.py at the DataBases field.

After everything is set you can use `python manage.py migrate` to build the models and `python manage.py populate_db` to insert entries from data.json in to the data base.

You can run the Django development server with `python manage.py runserver`. 

Functionality
---

With the server running you can enter 127.0.0.1:8000 and use the UI to input a location's longitude and latitude and request the closest cars. The server will responde with the 10 closest. Or you can Just sent a GET request
with the form `/cars?location=lng,lat` and the server will respond with a json object contain a list of the ten closest.
