# TODO исправить!!!!!!!!


.PHONY: list install install_dev lint run run_all tests run tests create_migration migrate downgrade
.DEFAULT_GOAL := list

list: ## Показать список всех команд
	@echo "Доступные команды:"
	@echo
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST) | sort

install: ## Установка зависимостей
	uv sync

install_dev: ## Установка зависимостей для разработчиков
	uv sync --all-groups
	uv run pre-commit install

lint: ## Запуск автоматического форматирование кода
	pre-commit run --all-files

run: ## Запуск приложения
	$(MAKE) migrate
	uv run app

run_all: ## Запуск контейнеров БД и приложения
	docker compose -f docker-compose.yaml up -d --wait
	$(MAKE) run

tests: ## Запуск тестов
	ENV_FOR_DYNACONF=test uv run pytest -v

run_tests: ## Запуск контейнеров БД и тестов
	docker compose -f docker-compose.test.yaml up -d --wait
	$(MAKE) tests
	docker compose -f docker-compose.test.yaml down

create_migration:
	@read -p "Введите описание ревизии: " msg; \
	uv run alembic revision --autogenerate -m "$$msg"

migrate:
	uv run alembic upgrade head

downgrade:
	uv run alembic downgrade -1
