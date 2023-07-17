up:
	docker compose -f docker-compose.yaml up -d
build:
	docker compose -f docker-compose.yaml up --build
down:
	docker compose -f docker-compose.yaml down && docker network prune --force