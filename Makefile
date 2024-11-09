run:
	poetry run python3 manage.py runserver
mig:
	poetry run python3 manage.py makemigrations
migrate:
	poetry run python3 manage.py migrate
user:
	poetry run python3 manage.py createsuperuser
static:
	poetry run python3 manage.py collectstatic
install:
	poetry add $(name)
app:
	poetry run python3 manage.py startapp $(name)
check:
	flake8
shell:
	poetry run python3 manage.py shell

index-build:
	poetry run python3 manage.py search_index --rebuild

