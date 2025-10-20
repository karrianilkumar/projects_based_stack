Creating a robust and user-friendly To-Do List application using Django involves several key steps, from setting up the project to implementing CRUD (Create, Read, Update, Delete) functionalities with intuitive user interfaces. Below is a comprehensive guide to help you build this application, ensuring high-quality code and design, suitable for a project valued at 5 lakhs.

1. Set Up the Django Project and Application

    Install Django: Ensure Django is installed in your environment.

pip install django

Create Project: Initialize a new Django project named django_todo.

django-admin startproject django_todo
cd django_todo

Create Application: Create a new app called todo.

python manage.py startapp todo

Register App: Add 'todo' to the INSTALLED_APPS in django_todo/settings.py.

    INSTALLED_APPS = [
        ...
        'todo',
    ]

2. Configure the Database

    Database Settings: In settings.py, configure the database to use PostgreSQL.

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'django_todo_db',
            'USER': 'your_username',
            'PASSWORD': 'your_password',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }

    Create Database: Ensure the PostgreSQL database django_todo_db is created.

3. Define the Model

    Task Model: In todo/models.py, define the Task model.

from django.db import models

class Task(models.Model):
    task_name = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.task_name

Migrate Models: Create and apply migrations.

    python manage.py makemigrations
    python manage.py migrate

4. Create Views and Templates

    Views: In todo/views.py, implement views for listing, adding, editing, and deleting tasks.

from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'todo/task_list.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'todo/add_task.html', {'form': form})

def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'todo/edit_task.html', {'form': form, 'task': task})

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'todo/delete_task.html', {'task': task})

Templates: Create templates (task_list.html, add_task.html, edit_task.html, delete_task.html) in todo/templates/todo/ directory.

    task_list.html:

        {% extends 'base.html' %}
        {% block content %}
        <h1>To-Do List</h1>
        <a href="{% url 'add_task' %}" class="btn btn-primary">Add Task</a>
        <ul>
            {% for task in tasks %}
            <li>
                {{ task.task_name }}
                <a href="{% url 'edit_task' task.id %}" class="btn btn-secondary">Edit</a>
                <a href="{% url 'delete_task' task.id %}" class="btn btn-danger">Delete</a>
            </li>
            {% endfor %}
        </ul>
        {% endblock %}

        add_task.html, edit_task.html, delete_task.html: Implement forms and confirmation prompts as needed.

5. Forms

    TaskForm: In todo/forms.py, create a form for the Task model.

    from django import forms
    from .models import Task

    class TaskForm(forms.ModelForm):
        class Meta:
            model = Task
            fields = ['task_name', 'completed']

6. URLs

    URL Configuration: In todo/urls.py, define URL patterns.

from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('add/', views.add_task, name='add_task'),
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
]

Include App URLs: In django_todo/urls.py, include the todo app URLs.

    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('todo.urls')),
    ]

7. Static Files and CSS

    Static Configuration: Ensure STATIC_URL and STATICFILES_DIRS are set
    
    
    
    
    
    
    
================================================================================================== >    
    
    
STATIC_URL = 'static/'

# below code need to be added in the settings.py file  : 
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]    
