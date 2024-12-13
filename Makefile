reset:
	$(MAKE) stop && $(MAKE) rm && $(MAKE) build && $(MAKE) run
build:
	docker compose -f docker-compose.dev.yml build
run:
	docker compose -f docker-compose.dev.yml up -d
logs:
	docker compose -f docker-compose.dev.yml logs
stop:
	docker compose -f docker-compose.dev.yml stop
rm:
	docker compose -f docker-compose.dev.yml down
exec:
	docker compose -f docker-compose.dev.yml exec grawards_api /bin/bash
test:
	docker compose -f docker-compose.dev.yml exec grawards_api pytest