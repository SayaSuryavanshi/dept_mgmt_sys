# dept_mgmt_sys

Setup Instructions

# Create virtual environment
python -m venv venv

# Activate it
venv\Scripts\activate    

# Install Django
pip install django

# Run Migrations
python manage.py makemigrations
python manage.py migrate

# Start Server
python manage.py runserver

