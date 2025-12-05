![version](https://img.shields.io/github/release/uc-cdis/psqlgraph.svg)
[![License](https://img.shields.io/github/license/uc-cdis/psqlgraph?logo=apache)](https://github.com/uc-cdis/psqlgraph/blob/master/LICENSE)


# Overview

The psqlgraph library is a layer on top of [SQLAlchemy's](http://www.sqlalchemy.org/) ORM layer that attemps to capitalize on the benefits of SQL while utilizing Postgresql's JSONB support for SQL-less flexibility.  Psqlgraph allows you to interact with your data graphically by defining Node and Edge models to maintain flexible many-to-many relationships.

# Usage

For usage documentation please see /doc/build/html.

# Installation

## Dependencies

Before continuing you must have the following programs installed:

- [Python 3.6](http://python.org/)
- [Postgresql 9.4](http://www.postgresql.org/download/)

The psqlgraph library requires the following dependencies

- [SQLAlchemy](http://www.sqlalchemy.org/)
- [Psycopg2](http://initd.org/psycopg/)

### Project Dependencies

Project dependencies are managed using [poetry](https://python-poetry.org/)

### Building Documentation

Documentation is built using [Sphinx](http://sphinx-doc.org/).

```
❯ cd doc
❯ make html
sphinx-build -b html -d build/doctrees   source build/html
Running Sphinx v1.2.3
     ...
dumping object inventory... done
build succeeded.

Build finished. The HTML pages are in build/html.
```

## Running tests locally

Run the setup script to create a test database:

```
python tests/ci_setup.py
```


Test with pytest

```
poetry run pytest -v tests
```

# Contributing
Read how to contribute [here](https://docs.gen3.org/gen3-resources/developer-guide/contribute/).
