# iCream

## Setup the project

Clone the project using Git.

```sh
https://github.com/rdtagline/iCream.git
cd iCream
```

### Create .env file

```sh
cp .env.sample .env
```

### Migrate the database

```sh
python manage.py migrate
```

### Create the super user

```sh
python manage.py createsuperuser
```

The project is now running on http://127.0.0.1:8000.

Hurray! Check on the http://127.0.0.1:8080
