from django.db import models

# Create your models here.

class Client(models.Model):
    email = models.CharField(max_length=100, primary_key=True, blank=False, null=False)
    fname = models.CharField(max_length=50, blank=False, null=False)
    lname = models.CharField(max_length=50, blank=False, null=False)
    password = models.CharField(max_length=100, blank=False, null=False)
    phone = models.CharField(max_length=9, blank=True, null=True)

    def __str__(self):
        return f'{self.fname} {self.lname}, email: {self.email}, phone: {self.phone}'

class Posn(models.Model):
    name = models.CharField(max_length=50, primary_key=True, blank=False, unique=True)
    salary = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return f'{self.name}, salary: {self.salary} PLN'
    
class Location(models.Model):
    id = models.AutoField(primary_key=True, unique=True, blank=False, null=False)
    street = models.CharField(max_length=255, blank=False, null=False)
    number = models.CharField(max_length=5, blank=False, null=False)
    postcode = models.CharField(max_length=6, blank=False, null=False)
    phone = models.CharField(max_length=9, blank=False, null=False, unique=True)

    def __str__(self):
        return f'{self.street}, {self.number}, {self.postcode}, phone: {self.phone}'

class Employee(models.Model):
    email = models.CharField(max_length=100, primary_key=True, blank=False, null=False)
    fname = models.CharField(max_length=50, blank=False, null=False)
    lname = models.CharField(max_length=50, blank=False, null=False)
    phone = models.CharField(max_length=9, blank=False, null=False)
    posn = models.ForeignKey(Posn, on_delete=models.CASCADE, blank=False, null=False)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, blank=False, null=False, default=1)

    def __str__(self):
        return f'{self.fname} {self.lname}, email: {self.email}, phone: {self.phone} | post: {self.posn} | {self.location}'

class Service(models.Model):
    id = models.IntegerField(primary_key=True, unique=True, blank=False, null=False)
    name = models.CharField(max_length=50, blank=False, null=False)
    price = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return f'{self.name}, price: {self.price} PLN'

class Record(models.Model):
    id = models.AutoField(primary_key=True, unique=True, blank=False, null=False)
    start_date = models.DateField(blank=False, null=False)
    deadline = models.DateField(blank=True, null=True, default='')
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f'start date: {self.start_date}, deadline: {self.deadline} | {self.client} | {self.service} | {self.location}'
