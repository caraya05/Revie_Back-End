up:
	python manage.py runserver

superuser:
	python manage.py createsuperuser

requirements:
	pip install -r requirements.txt
	pip freeze > requirements.txt

shell:
	python manage.py shell

export_data:
	python manage.py dumpdata --indent 4 > fixture.json

import_data:
	python manage.py loaddata fixture.json

migrate:
	python manage.py makemigrations
	python manage.py migrate

clean_data: export_data
	python manage.py flush

test:
	python manage.py test --no-input --parallel

app:
	python manage.py startapp $(name)

start: requirements migrate import_data superuser export_data
	python manage.py makemigrations
	python manage.py migrate

statics:
	python manage.py collectstatic --no-input

messages:
	python manage.py makemessages -l 'es'
	python manage.py makemessages -l 'en'

compilemessages:
	python manage.py compilemessages -f

pylint:
	pylint  *.py