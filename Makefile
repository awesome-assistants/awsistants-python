#!make

all: install download lint test build

install:
	poetry lock
	poetry install --with test,dev

download:
	wget -O awsistants/assistants.json https://raw.githubusercontent.com/awesome-assistants/awesome-assistants/main/build/assistants.json

lint:
	poetry run black .

test:
	poetry run pytest

build:
	poetry build

changelog:
	poetry run towncrier build --yes --version v$(shell poetry version -s)

publish-test:
	poetry build
	poetry config repositories.testpypi https://test.pypi.org/legacy/
	poetry publish --no-interaction -r testpypi -u __token__ -p ${PYPI_TOKEN}

clean:
	rm -rf dist
	rm -rf .pytest_cache
	rm -rf poetry.lock
	find . -type f -name '*.pyc' -delete

.PHONY: all download build lint test clean
