# The blog with django

[![License](https://img.shields.io/badge/License-MIT-blue)](https://github.com/FedericoBruzzone/IP_DRM_for_IEEE1599standard/edit/master/License)
[![Python](https://img.shields.io/badge/Python-v3.8.8-green)](https://docs.python.org/3/)
[![Django](https://img.shields.io/badge/Django-v4.0.6-blue)](https://www.djangoproject.com/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-v4.4-orange)](https://www.djangoproject.com/)
[![stability-stable](https://img.shields.io/badge/stability-stable-green.svg)](https://github.com/emersion/stability-badges#stable)

# Introduction
A blog with django

In this repository there is the implementation in django of a blog. It was created to learn how to use Django framework in addition to why I would like to open a blog to talk about computer science, music and critical thinking. The main language for the development back end is python, as it is in progress the part of front end is still to be developed in the correct way, for the moment is used bootstrap for a first "look".

---

# Setup 
1. Install [Visual studio Code](https://visualstudio.microsoft.com) or your favourite text editor

2. Install [git](https://github.com/git-guides/install-git). 

    I would recommend you to use git bash to run terminal commands.

3. Intall [python](https://www.python.org/downloads/). 

    I would recommend you to install [3.8.8](https://www.python.org/downloads/release/python-388/) version.

4. If you are on MacOS I would racommend to intall pip package management system.

    ```
    $ sudo easy_install pip
    ```
---

## First step
Now, you can fork or clone this repository and in the folder you can try to set up the python development environment.

Window:
```
$ python -m venv virt
```

MacOS:
```
$ sudo pip install virtualenv
```
```
$ virtualenv thanos
```
```
$ cd thanos
```
---

## Second step
You should want to turn on your virtual environment.

Window:
```
$ source virt/Scripts/activate
```

After this, I would racommend to run a server to digit:
```
$ cd ablog
```

MacOS:
```
$ source bin/activate
```

---

## Third step
Now, you have to install Django.

Window:
```
$ pip intall django==4.0.6
```
MacOS:
```
$ sudo pip install django==4.0.6
```

---

## Command for windows users
Start and setup a new django project

Maybe the command `manage.py` could be only `manage`

```
$ django-admin.py startproject --project_name--
```

```
$ cd --project_name--
```

Preps your database for migration

```
$ python manage.py makemigrations
```

Execute your migration & updates the database
```
$ python manage.py migrate
```

---

Run a server

Maybe the command `manage.py` could be only `manage`

```
$ python manage.py runserver
```

And now write on your favorite browser `localhost:8000`

---

Create a user with admin level premissions

Maybe the command `manage.py` could be only `manage`

```
$ winpty python manage.py createsuperuser 
```

---

Create app folder and files

Maybe the command `manage.py` could be only `manage`

```
$ python manage.py startapp --app_name--
```

In this case the app_name is `theblog` on the firsr folder ablog

After this, you should add in INTALLED_APPS on --project_name--/--project_name--/setting.py file the line 
```python
'--name--',
```

And, you should add in urlpatterns on --project_name--/--project_name--/urls.py the line

```python
path('', include('--app_name--.urls')),
```

And add at the end of the line `from django.urls import path` the `include` modules like this: 

```python
from django.urls import path, include
```

Now, you should create a `utils.py` file on --app_name-- folder like this:
```python
from django.urls import path
from . import views

urlpatterns = [
    path('''...''')
]
```

---
Generate your random django secret key.

```
$ python manage.py shell
```

In the shell:

```python
$ from django.core.management.utils import get_random_secret_key
```

```python
$ print(get_random_secret_key())
```

---

# Troubleshooting
If you find problems with the source code or configuration, please contact me at federico.bruzzone.i@gmail.com.


