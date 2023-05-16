from django.contrib import admin
from .models import Client, Employee, Post, Service, Record

# Register your models here.

admin.site.register(Client)
admin.site.register(Employee)
admin.site.register(Post)
admin.site.register(Service)
admin.site.register(Record)
