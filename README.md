# iCream

## Setup the project

Clone the project using Git.

```sh
git clone git@github.com:rdtagline/iCream.git
cd iCream
```

### Run the docker containers

```sh
docker-compose up -d --build
```

### Migrate the database

```sh
docker-compose exec web python manage.py migrate
```

### Create the super user

```sh
docker-compose exec web python manage.py createsuperuser
```

The project is now running on http://127.0.0.1:8000
