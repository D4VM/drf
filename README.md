# Django-REST-Framework-Angular-Example

This is an example project for Django Rest Framework. This project is a simple store where you can browse products and place orders. The backend is built using Django Rest Framework 

## Installation

1. Clone the repository
2. Create a virtual environment `python3 -m venv .venv` and activate it `source .venv/bin/activate`
3. Install the requirements `pip install -r requirements.txt`
4. Migrate CustomUser first `python manage.py migrate user`
4.1 Migrate Database `python3 manage.py migrate`
4.2 Create a SuperUser `python3 manage.py createsuperuser`

5. Run the development server `python manage.py runserver`

## Running the Project

1. Open a web browser and go to `http://localhost:8000/api/docs`


## Project Stucture

├── app
│   # Main Django settings
│
├── media
│   # Media folder for product images
│
├── order
│   # Order app
│
├── product
│   # Product app
│
├── user
│   # Custom User app
│
├── requirements.txt
│   # Requirements
│
├── manage.py
│   # Djano manage script
│
├── schema.yml
│   # Swagger-ui schema
│


