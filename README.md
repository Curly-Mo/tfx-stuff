# tfx-stuff

[![Build Status](https://travis-ci.org/Curly-Mo/tfx-stuff.svg?branch=master)](https://travis-ci.org/Curly-Mo/tfx-stuff)
[![Coverage](https://coveralls.io/repos/github/Curly-Mo/tfx-stuff/badge.svg)](https://coveralls.io/github/Curly-Mo/tfx-stuff)
[![Documentation](https://readthedocs.org/projects/tfx-stuff/badge/?version=latest)](https://tfx-stuff.readthedocs.org/en/latest/?badge=latest)
[![PyPI](https://img.shields.io/pypi/v/tfx-stuff.svg)](https://pypi.python.org/pypi/tfx-stuff)
[![PyPI Pythons](https://img.shields.io/pypi/pyversions/tfx-stuff.svg)](https://pypi.python.org/pypi/tfx-stuff)
[![License](https://img.shields.io/pypi/l/tfx-stuff.svg)](https://github.com/Curly-Mo/tfx-stuff/blob/master/LICENSE)

tfx stuff

## Features

* What it do?

## Usage

* TODO

## Install

```console
pip install tfx-stuff
```

## Documentation
See https://tfx-stuff.readthedocs.org/en/latest/

## Development
```console
pip install poetry
cd tfx-stuff
poetry install
```
### Run
To run cli entrypoint:
```console
poetry run tfx_stuff --help
```

### Tests
```console
poetry run tox
```

### Docker
To run with docker
```console
docker build -t tfx-stuff .
docker run tfx_stuff:latest tfx_stuff --help
```
