# Yiatour API
Yiatou API

## Installation

- Clone the project:
```sh
git clone https://github.com/samnklcf/yiatouback.git
```

- Create your own virtual environment:

```sh
python3 -m venv venv
source .venv/Scripts/activate
```

 - Install your requirements
```sh
pip install -r requirements.txt
```

 - Make your migrations
```sh
python manage.py makemigrations
python manage.py migrate
```

 - Create a new superuser
```sh
python manage.py createsuperuser
```

 - Run the server
```sh
python manage.py runserver
```

## Usage

To use the API, you just need to open [Postman](https://www.postman.com/) and then go to the following url:


```sh
http://localhost:8000/v1/the-resource-you-want
```

## Documentation

You can find the API documentation on :
```sh
http://localhost:8000/swagger/
```

## Happy Coding !!!