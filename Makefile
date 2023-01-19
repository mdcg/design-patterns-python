create-virtualenv:
	python -m venv env
	@echo "Run the following command to activate your virtualenv: source env/bin/activate"

poetry-setup:
	pip install pip -U
	pip install setuptools
	pip install poetry

poetry-install-dependencies:
	poetry install

setup: poetry-setup poetry-install-dependencies

tests: setup
	poetry run python -m pytest --cov=creational --cov-report term --cov-report html --no-cov-on-fail --cov-fail-under=95

tests-coverage-html-server:
	python -m http.server 8000 -d htmlcov

format:
	black -l 120 . --exclude env
