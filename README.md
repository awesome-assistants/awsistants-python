# Awsistants python package

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Install

### pip

    pip install awsistants@git+https://github.com/awesome-assistants/awsistants-python@main

### requirements.txt

    awsistants@git+https://github.com/awesome-assistants/awsistants-python@main

### poetry

    poetry add git+https://github.com/awesome-assistants/awsistants-python.git@main

or add to `pyproject.toml`

    awsistants = {git = "https://github.com/awesome-assistants/awsistants-python.git", rev = "main"}

## Build

    make

## Usage

```python

from awsistants import Awsistants

aw = Awsistants()
all_assistants = aw.get_assistants()
awesome_assistant = all_assistants[0]

print(awesome_assistant.id)
print(awesome_assistant.name)
print(awesome_assistant.instructions)

```