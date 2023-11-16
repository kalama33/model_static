## Django Exercise: Creating and Displaying a Simple Model with Static CSS### Objective:

To create a simple Django app that:

1. Has a basic model.
2. Allows users to add entities to this model via the Django admin interface.
3. Displays these entities using a `ListView`.
4. Adds static CSS to style the displayed list.### Task:1. * **Set up the Django Project and App** *:
   - Create a new Django project called `myproject`.
   - Create a new app called `myapp`.2. * **Design a Simple Model** *:
   - In `myapp/models.py`, design a simple model called `Item` with a single `CharField` named `name`.3. * **Setup Django Admin** *:
   - Register the `Item` model with the Django admin in `myapp/admin.py`.
   - Create a superuser and then use the admin interface to add 3 entities to the `Item` model.4. * **Display the Model Data** *:
   - Use a `ListView` to display the entities in a template.
   - Add static CSS to style this list.---### Instructions:1. * **Set up the Django Project and App** *:

```
bash
    django-admin startproject myproject
    cd myproject
    python manage.py startapp myapp
  
```

2. * **Design a Simple Model** *:    `myapp/models.py`:

```
python
....
  
```

3. * **Setup Django Admin** *:    `myapp/admin.py`:

```
python
    from django.contrib import admin
    from .models import Item

    ....
  
```

    - Now, add`myapp` to `INSTALLED_APPS` in `myproject/settings.py`:

```
python
    INSTALLED_APPS = [
        ...
       ......
    ]
  
```

    - Run migrations to create the database table for the`Item` model:

```
bash
    python manage.py makemigrations
    python manage.py migrate
  
```

    - Create a superuser to access the admin interface:

```
bash
    python manage.py createsuperuser
  
```

    - Run the server and access the admin site at`<a target="_blank" class="c-link" data-stringify-link="http://localhost:8000/admin/" delay="150" data-sk="tooltip_parent" href="http://localhost:8000/admin/" rel="noopener noreferrer">http://localhost:8000/admin/</a>`. Login with the superuser credentials and add 3 items to the `Item` model.4. * **Display the Model Data** *:    `myapp/views.py`:

```
python
    from django.views.generic import ListView
    from .models import ......
.....
  
```

    - Create a`templates` directory inside `myapp` and then create a file named `item_list.html`.    `myapp/templates/item_list.html`:

```
html
    <!DOCTYPE html>
    <html>
    <head>
        <title>Item List</title>
        <link rel="stylesheet" type="text/css" href="{% static 'styles.css' %}">
    </head>
    <body>
        <ul>
        .......
        </ul>
    </body>
    </html>
  
```

    - Now, setup static files. First, create a`static` directory inside `myapp`. Inside this directory, create a CSS file named `styles.css`.    `myapp/static/styles.css`:

```
css
    body {
        font-family: Arial, sans-serif;
        background-color: #f4f4f4;
    }
    ul {
        list-style-type: none;
        padding: 20px;
    }
    li {
        background-color: #e0e0e0;
        padding: 10px;
        margin: 5px 0;
    }
  
```

    - also add a red border around ul tag    - Lastly, update the project's`urls.py` to include the `ItemListView`:    `myproject/urls.py`:

```
python
    from django.urls import path
    from myapp.views import ItemListView

    urlpatterns = [
        path('items/', ....., name='item-list'),
        ...
    ]
  
```

    - add the urls.py to the main urls.py5. ***Run and Test** *:    - Start the Django server:

```
bash
    python manage.py runserver
  
```

    - Access the item list at`<a target="_blank" class="c-link" data-stringify-link="http://localhost:8000/items/" delay="150" data-sk="tooltip_parent" href="http://localhost:8000/items/" rel="noopener noreferrer">http://localhost:8000/items/</a>`. You should see the 3 items you added via the admin interface, styled with the provided CSS.
