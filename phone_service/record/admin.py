from django.contrib import admin
from .models import Client, Employee, Posn, Service, Record, Location

# Register your models here.

admin.site.register(Client)
admin.site.register(Employee)
admin.site.register(Posn)
admin.site.register(Service)
admin.site.register(Record)
admin.site.register(Location)
