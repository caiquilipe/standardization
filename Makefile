build-compose:
	docker-compose build

down-compose:
	docker-compose down

up-compose:
	docker-compose up -d
	make migrate

update:
	make build-compose
	make up-compose

logs-compose:
	docker-compose logs -f

test-compose:
	docker-compose exec web python manage.py test

migrate:
	docker-compose exec web python manage.py migrate

superuser:
	docker-compose exec web python manage.py createsuperuser

gunicorn-start:
	./gunicorn_start



