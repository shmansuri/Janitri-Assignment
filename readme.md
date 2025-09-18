# Janitri Backend Assignment

This is my backend assignment made using Django and Django REST Framework.
It has user registration and login, patient management and heart rate recording API.

## Features

1. User registration and JWT login
2. Add and view patients
3. Record and fetch heart rate data of patient
4. Authentication required for patient and heart rate APIs
5. Pagination in list APIs


## Tech Stack

Python 3.10
Django 5.0
Django REST Framework
Simple JWT (for login tokens)
SQLite database (default)


## Setup Instructions

1. Clone the repo

   git clone https://github.com/shmansuri/JANITRI-ASSIGNMENT.git

   cd JANITRI-ASSIGNMENT

2. pip install -r requirements.txt

3. Run migrations

4. Run server  http://127.0.0.1:8000/

API Endpoints

/api/auth/register/ -> Register new user
/api/auth/login/ -> Login and get JWT token

For Patients 

GET /api/patients/ -> List patients (need login)
POST /api/patients/ -> Add new patient (need login)
GET /api/patients/<id>/ -> Get patient details

Heart Rate

/api/patients/<id>/heartrate/ -> Add heart rate for patient(POST)
/api/patients/<id>/heartrate/ -> List heart rates of patient(GET)


APIs Test 

1. Register user -> http://127.0.0.1:8000/api/auth/register/

   in json form
   {
     "username": "username",
     "email": "<user_Email>",
     "password": "<Password>",
     "role":"<Enter Your Role>"
   }

2. Login User ->  http://127.0.0.1:8000/api/auth/token/

{
  "username": "<username>",
  "password": "<Password123>"
}



Copy the access token from login response.


### In Postman


open the API request you want to test (e.g., /api/patients/).

Go to the Authorization tab.

Select Bearer Token from the dropdown.

Paste the copied token into the token field.

Now send the request — it will work if the token is valid.

## API Documentation
See [apidoc.txt](./apidoc.txt) for full API documentation with request/response examples.


Made by Saddam Hussain Mansuri as part of Janitri assignment.
