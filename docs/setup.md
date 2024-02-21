# Setup Instructions

## Create and Activate Virtual Environment
First, create a virtual environment by running `python -m venv venv`. 
    
Then, activate the virtual environment by running `source venv/bin/activate` on Mac or `venv\Scripts\activate` on Windows.

## Install Dependencies
First, install the dependencies by running `pip install -r requirements.txt`.

## Create .env File

Create a `.env` file in the root of the project and add the variables as defined in the `.env.example` file under "development"

## Create Database

This project uses PostgreSQL as the database. First, install PostgreSQL and create a database. Add the local database settings to the `.env` file.

Sample settings can be found in the `.env.example` file under "development".

## Run Migrations

Run `python manage.py migrate` to populate your empty database with the database tables.

## Create Super User
First, run `python manage.py createsuperuser` to create a super user. This will allow you to log into the admin panel. 

Note: this will ask you for an email address instead of a user name, since we have changed the user model to use the email field as the unique identifier for the user.

## Run Server
Finally, run `python manage.py runserver` to start the development server. You can access the admin panel at `http://127.0.0.1:8000/admin/`. You login with the super user you created in the previous step.