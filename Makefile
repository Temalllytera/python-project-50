lint:
	poetry run ruff check gendiff tests  # Основная команда линтинга
	poetry run ruff format --check gendiff tests  # Проверка форматирования

format:
	poetry run ruff format gendiff tests  # Автоформатирование кода

test:
	poetry run pytest -v

coverage:
	poetry run pytest --cov=gendiff --cov-report xml
