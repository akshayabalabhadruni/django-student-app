# Django Student Management App

A web application built with Python and the Django framework. This project demonstrates core Django concepts including the Model-View-Template (MVT) architecture, database routing via the Django ORM, and the built-in administrative interface.

## Core Technologies
* **Framework:** Django (Python)
* **Database:** SQLite (Default)
* **Architecture:** MVT (Model-View-Template)

## Project Structure
* `manage.py`: The command-line utility for Django administrative tasks.
* `project_folder/`: Contains the main `settings.py` and global `urls.py` routing.
* `app_folder/`: Contains the `models.py` (database schema), `views.py` (business logic), and specific app routing.

## Setup Instructions

**1. Clone the repository**
```bash
git clone [https://github.com/akshayabalabhadruni/django-student-app.git](https://github.com/akshayabalabhadruni/django-student-app.git)
cd django-student-app
```

**2. Install dependencies**
Make sure Python is installed, then install Django:
```bash
pip install django
```

**3. Initialize the Database (Migrations)**
Apply the database schema to create your local SQLite database:
```bash
python manage.py makemigrations
python manage.py migrate
```

**4. Create an Admin Account (Optional)**
Generate a superuser to access the Django admin panel:
```bash
python manage.py createsuperuser
```

**5. Run the Server**
Launch the local development server:
```bash
python manage.py runserver
```

**6. Access the Application**
* Main app: `http://127.0.0.1:8000/`
* Admin panel: `http://127.0.0.1:8000/admin/`
