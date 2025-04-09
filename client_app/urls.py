from django.urls import path
from .views import create_employee

urlpatterns = [
    path('create-employee/<name>', create_employee, name="create_employee")
]