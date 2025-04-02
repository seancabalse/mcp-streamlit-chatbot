# Docker Compose file path
DC_FILE := docker/docker-compose.yml

# Default target
.DEFAULT_GOAL := help

.PHONY: help build up down logs clean ps

# Show help
help:
	@echo "Available commands:"
	@echo "  make build    - Build the containers"
	@echo "  make up       - Start the containers in detached mode"
	@echo "  make down     - Stop and remove the containers"
	@echo "  make logs     - Show logs from all containers"
	@echo "  make clean    - Remove all containers, images, and volumes"
	@echo "  make ps       - List all running containers"
	@echo "  make rebuild  - Rebuild and restart containers"

# Build the containers
build:
	docker-compose -f $(DC_FILE) build

# Start the containers in detached mode
up:
	docker-compose -f $(DC_FILE) up -d

# Stop and remove the containers
down:
	docker-compose -f $(DC_FILE) down

# Show logs from all containers
logs:
	docker-compose -f $(DC_FILE) logs -f

# Remove all containers, images, and volumes
clean:
	docker-compose -f $(DC_FILE) down -v --rmi all

# List all running containers
ps:
	docker-compose -f $(DC_FILE) ps

# Rebuild and restart containers
rebuild:
	docker-compose -f $(DC_FILE) down
	docker-compose -f $(DC_FILE) build --no-cache
	docker-compose -f $(DC_FILE) up -d

# Start containers in foreground mode (with logs)
up-logs:
	docker-compose -f $(DC_FILE) up

# Restart containers
restart:
	docker-compose -f $(DC_FILE) restart

# Show logs for a specific service
# Usage: make service-logs SERVICE=streamlit-app
service-logs:
	docker-compose -f $(DC_FILE) logs -f $(SERVICE)

# Execute a command in a container
# Usage: make exec SERVICE=streamlit-app CMD=bash
exec:
	docker-compose -f $(DC_FILE) exec $(SERVICE) $(CMD) 