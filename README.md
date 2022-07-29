# The blog with django

[![Python](https://img.shields.io/badge/Python-3.8.8-orange)](https://docs.python.org/3/)
[![Django](https://img.shields.io/badge/Django-4.0.6-orange)](https://www.djangoproject.com/)
[![stability-stable](https://img.shields.io/badge/stability-stable-green.svg)](https://github.com/emersion/stability-badges#stable)

# Introduction


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
...

---

## Input for windows users
Start and setup a new django project

Maybe the command `migrate.py` could be only `migrate`

```
$ django-admin.py startproject --project_name--
```

```
$ cd --project_name--
```

```
$ python manage.py migrate
```

```
$ python manage.py runserver
```

And now write on your favorite browser `localhost:8000`

---

Create admin user (super user)

Maybe the command `migrate.py` could be only `migrate`

```
$ winpty python manage.py createsuperuser 
```

---

Start application

Maybe the command `migrate.py` could be only `migrate`

```
$ python manage.py startapp --app_name--
```

In this case the app_name is `theblog` on the firsr folder ablog

After this, you have to add in INTALLED_APPS on ablog/ablog/setting.py file the line 
```python
'--name--',
```

And, you have to add in urlpatterns

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



---

# Troubleshooting
If you find problems with the source code or configuration, please contact me at federico.bruzzone.i@gmail.com.


