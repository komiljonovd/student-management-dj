python -m venv venv
source venv/bin/activate  # Для Linux/macOS
venv\Scripts\activate     # Для Windows

pip install -r requirements.txt

python manage.py makemigrations studentapp
python manage.py migrate
python manage.py createsuperuser 

python manage.py runserver

pytest # for testing
pytest --verbose # for testing




