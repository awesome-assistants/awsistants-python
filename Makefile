#!make

all: install download lint test release build

install:
	poetry install --with test

download:
	wget -O awsistants/assistants.json https://raw.githubusercontent.com/awesome-assistants/awesome-assistants/main/build/assistants.json

lint:
	poetry run black .

test:
	poetry run pytest

release:
	poetry version patch

version:
	poetry version --short

build:
	poetry build

publish:
	poetry publish

clean:
	rm -rf dist
	rm -rf .pytest_cache
	rm -rf poetry.lock
	find . -type f -name '*.pyc' -delete

.PHONY: all download build lint test clean
