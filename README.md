# Introduction

TODO: Give a short introduction of your project. Let this section explain the objectives or the motivation behind this project.

# Getting Started

TODO: Guide users through getting your code up and running on their own system. In this section you can talk about:

1. Installation process
2. Software dependencies
3. Latest releases
4. API references

# Important Commands

- to create requirement.txt

```python
    pip list --format=freeze > requirements.txt
```

- schema based alembic make migration

```
alembic -x tenant=SCHEMA revision -m "comment" --autogenerate
```

- schema based alembic migrate

```cmd migrate
alembic -x tenant=SCHEMA upgrade head
```

- to generate table schema

```
sqlacodegen postgresql:///some_local_db
```

- to freeze requirements
```
pip list --format=freeze > requirements.txt
```
- To run a main server 
```
uvicorn app.main:app --reload
```
