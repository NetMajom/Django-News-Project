# Django News App

The goal of this news project is to provide minimalistic django project  that everyone can use, which just works out of the box and has the basic setup you can expand on.

### Features

* Custom User Model
* Article, and Comment model
* Used Bootstrap 4.6.0 with CDN
* User registration, and login
* Create, modify, and delete articles
* Create comments inside to article
* Include custom password forget, password reset
* Password reset email sending with Gmail
* SQLite by default

## Getting Started

Setup project environment with virtualenv and pip.

```bash
$ virtualenv project-env
$ source project-env/bin/activate
$ pip install -r https://raw.githubusercontent.com/netmajom/Django-News-Project/master/requirements.txt

# You may want to change the name `projectname`.
$ django-admin startproject --template https://github.com/netmajom/Django-News-Project/archive/master.zip projectname

$ cd projectname/
$ cp settings_custom.py.edit settings_custom.py
$ python manage.py makemigrations
$ python manage.py migrate
# Only if you want to use the Django admin
$ python manage.py createsuperuser
$ python manage.py runserver
```

## Contributing

Feel free to fix bugs, improve things, provide documentation. Just send a pull request.