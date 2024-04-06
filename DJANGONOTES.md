# Django - Snippets and Syntax

Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design.

## Installation

Assuming you have Python installed on your computer, you can use the package manager [pip](https://pip.pypa.io/en/stable/) to install Django.

```bash
pip install django
```

## Running the Server

```python
python manage.py runserver
```
Enter this command to run a local development server on your computer, that updates in real-time once you make changes to the code.
```Performing system checks...

System check identified no issues (0 silenced).

You have unapplied migrations; your app may not work properly until they are applied.
Run 'python manage.py migrate' to apply them.

March 26, 2024 - 15:50:53
Django version 5.0, using settings 'mysite.settings'
Starting development server at http://127.0.0.1:8000/ 
Quit the server with CONTROL-C.
```

With that, the server’s running. Visit http://127.0.0.1:8000/ or http://localhost:8000 with your web browser.

# Import CSS / JS / Images in Django:
In Django, files like these are called as static files. In order to load them in the Django application, you must first  add this block of code in the first line of every template / html file (before DOCTYPE! html)

```bash
{% load static %}
```
