# Installation

Installation is very easy.

## Using a virtual environment to install dependencies

Using the `venv` module that is now part of the standard library (python 3.3+).

### For Windows

```sh
# creating the virtual env
$ python3 -m venv <your_env_dir>
# activating the environment
$ venv\scripts\activate
```

## Installing dependencies

```sh
$ pip install -r requirements.txt
```

Add `'rest_framework'` to your `INSTALLED_APPS` setting.

    INSTALLED_APPS = [
        ...,
	    'rest_framework',
	    'rest_framework.authtoken',
	    'core',
    ]


# Db migration

The configured database is sqlite (just for demonstration purposes)

```sh
$ python manage.py migrate
# create an administrator account
$ python manage.py createsuperuser --email admin@example.com --username admin
```
# Create a token for the superuser from the command line
```sh
$ python manage.py drf_create_token admin
```

# Run the app

```sh
$ python manage.py runserver
```


# Site URLs

Admin site: `http://localhost:8000/admin`

## Endpoints
The application has only one endpoints:

```sh
/api/messages/ - POST - To create a message
```



# Contributors
```json
{
  "Oyebami Festus":{
    "repository": "https://github.com/Festorah/my-dash",
    "email":"festusoyebami@gmail.com"
  }
}
```

## License

Copyright © Oyebami Festus. Licensed under the [Apache License](/LICENSE).
