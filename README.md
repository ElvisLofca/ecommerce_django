# Instructions

## Folders structure and explanation
- django_todo
  - **api** *(application)*
    - tests *(folder of tests separated by logic)*
  - **core** *(core of the project)*
    - custom *(folder of custom exception and error messages)*
    - settings *(folder of settings divided in use cases)*

## Running project without docker

In this case we want to start the project without docker. In order to do that we have to install the virtual environment, create and activate it. At this point run:

```shell
pip install requirements.txt
```

### settings.dev

```shell
python manage.py makemigrations
```

```shell
python manage.py migrate
```

```shell
python manage.py runserver
```

### settings.prod
keep in mind that this is for demonstrations only, when your website is hosted to a vps you will configure it to run in production without passing the settings parameters.

```shell
python manage.py makemigrations --settings=core.settings.prod
```

```shell
python manage.py migrate --settings=core.settings.prod
```

```shell
python manage.py runserver --settings=core.settings.prod
```

## Running project with docker

```shell
docker build -t image_name:tag_name .
```

```shell
docker run -p 8000:8000 --rm --name container_name image_name:tag_name  
```

```shell
docker start -i container_name
```

```shell
docker exec -it container_name /bin/bash
```


## Tests
If we want to execute our test we must enter this command and optionally we can add the name of the app we want to test for example api

```shell
python manage.py test  
```

## Test Coverage
If you want to check how much of your code has been tested run:

- To execute the coverage script
  ```shell
  coverage run --source='.' test api (this is the app name)   
  ```

- To generate a shell report
  ```shell
  coverage report  
  ```
  
- To generate an html report
  ```shell
  coverage report  
  ```
  
For more information about coverage check the [coverage documentation](https://coverage.readthedocs.io/en/7.3.2/).
