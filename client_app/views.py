from rest_framework import generics
from django.http import HttpResponse
from .models import Employee
def create_employee(request, name):
    employee = Employee(name=name)
    employee.save()
    return HttpResponse(f"Employee {name} created.")