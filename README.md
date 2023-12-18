# ProductMicroService 
#Package Installation
pip install django
pip install djangorestframework
pip install djongo
pip install Django psycopg2
pip install graphene-django
pip install django-import-export
pip install django-cors-headers
python manage.py migrate
python manage.py createsuperuser
python manage.py makemigrations
python manage.py runserver

# Database Configuration
ProductMicroService\product_api\settings.py

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'product_app',
    }
}

