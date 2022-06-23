# iCream

## Setup the project

Clone the project using Git.

```sh
git clone git@github.com:rdtagline/iCream.git
cd iCream
```

### Create .env file

```sh
cp .env.sample .env
```

### Install

```sh
pip install -r requirements.txt
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
