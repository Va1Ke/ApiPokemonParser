# pokemonApiParser

* Update requirements:
```
pip freeze > requirements.txt
```

* Make migrations:
```
alembic revision --autogenerate -m "<migration_name>"
alembic upgrade head
```

* Use parser:
```
python -m app.main
```

### Set environment variables:
* list of environment variables which should be set:
```
POSTGRES_USER
POSTGRES_PASSWORD
POSTGRES_HOST
POSTGRES_PORT
POSTGRES_DB
```


**Windows:**
```
//CMD:
set SOME_VARIABLE=some_value

//Powershell:
$Env:Foo = 'An example'
```
**Linux:**
```
export SOME_VARIABLE=some_value
```

