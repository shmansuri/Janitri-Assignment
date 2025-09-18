# Janitri Backend Assignment

This is my backend assignment made using Django and Django REST Framework.
It has user registration and login, patient management and heart rate recording API.

## Features

* User registration and JWT login
* Add and view patients
* Record and fetch heart rate data of patient
* Authentication required for patient and heart rate APIs
* Pagination in list APIs

---

## Tech Stack

* Python 3.10
* Django 5.0
* Django REST Framework
* Simple JWT (for login tokens)
* SQLite database (default)

---

## Setup Instructions

1. Clone the repo

   ```bash
   git clone https://github.com/shmansuri/janitri-assignment.git
   cd janitri-assignment
   ```

3. Install requirements

   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations

5. Run server

http://127.0.0.1:8000/

API Endpoints

 Auth

* /api/auth/register/ → Register new user
* /api/auth/login/ → Login and get JWT token

 For Patients

* GET /api/patients/ → List patients (need login)
* POST /api/patients/ → Add new patient (need login)
* GET /api/patients/<id>/ → Get patient details



 Heart Rate

* `POST /api/patients/<id>/heartrate/` → Add heart rate for patient
* `GET /api/patients/<id>/heartrate/` → List heart rates of patient

---

## How to Test APIs

1. Register user → `/api/auth/register/`

   ```json
   {
     "username": "username",
     "email": "<user_Email>",
     "password": "<Password>"
   }
   ```

2. /api/auth/login/ -> Login
   Copy the `access` token from response.

Made by **\Saddam Hussain Mansuri** as part of Janitri assignment.
