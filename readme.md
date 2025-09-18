# Janitri Backend Assignment

This is my backend assignment made using Django and Django REST Framework.
It has user registration and login, patient management and heart rate recording API.

---

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
   git clone https://github.com/<your-username>/janitri-assignment.git
   cd janitri-assignment
   ```

2. Create virtual environment

   ```bash
   python -m venv venv
   venv\Scripts\activate   # for windows
   source venv/bin/activate  # for linux/mac
   ```

3. Install requirements

   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Run server

   ```bash
   python manage.py runserver
   ```

Server will start at `http://127.0.0.1:8000/`

---

## API Endpoints

### Auth

* `POST /api/auth/register/` → Register new user
* `POST /api/auth/login/` → Login and get JWT token

### Patients

* `GET /api/patients/` → List patients (need login)
* `POST /api/patients/` → Add new patient (need login)
* `GET /api/patients/<id>/` → Get patient details

### Heart Rate

* `POST /api/patients/<id>/heartrate/` → Add heart rate for patient
* `GET /api/patients/<id>/heartrate/` → List heart rates of patient

---

## How to Test APIs

1. Register user → `/api/auth/register/`

   ```json
   {
     "username": "testuser",
     "email": "test@example.com",
     "password": "testpass"
   }
   ```

2. Login → `/api/auth/login/`
   Copy the `access` token from response.

3. In Postman (or any tool), set header:

   ```
   Authorization: Bearer <your_access_token>
   ```

4. Now you can call patient and heart rate APIs.

---

## Notes

* Used SQLite for database (no need to install extra db).
* Default Django User model used.
* `created_by` field in patient is auto linked with logged in user.
* JWT access token is required for all protected APIs.

---

Made by **\[Your Name]** as part of Janitri assignment.
