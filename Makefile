COMPOSE=docker-compose -f

up:
	$(COMPOSE) $(c)/docker-compose.yml up -d

logs:
	$(COMPOSE) $(c)/docker-compose.yml logs -f --tail 100

down:
	$(COMPOSE) $(c)/docker-compose.yml down
