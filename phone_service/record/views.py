from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    clients = Client.objects.all()
    employees = Employee.objects.all()
    posts = Posn.objects.all()
    services = Service.objects.all()
    records = Record.objects.all()
    locations = Location.objects.all()
    context = {
            'clients':clients,
            'employees':employees,
            'posts':posts,
            'services':services,
            'records':records,
            'locations':locations
            }
    return render(request, "record/index.html", context)
