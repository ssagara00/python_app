SERVICE_NAME := mypythonapp-web-1

build:
	docker compose up -d --build
down:
	docker compose down
up:
	docker compose up -d
exec:
	docker container exec -it ${SERVICE_NAME} /bin/bash
