from django.db import models

# Create your models here.

class Client(models.Model):
    client_email = models.CharField(max_length=100, primary_key=True, blank=False)
    client_fname = models.CharField(max_length=50, blank=False)
    client_lname = models.CharField(max_length=50, blank=False)
    client_pass = models.CharField(max_length=100, blank=False)
    client_phone = models.CharField(max_length=9, blank=True, default='')

    def __str__(self):
        return f'{self.client_fname} {self.client_lname}, email: {self.client_email}, phone: {self.client_phone}'

class Post(models.Model):
    post_name = models.CharField(max_length=50, primary_key=True, blank=False, unique=True)
    post_salary = models.FloatField(default=2000.00)

    def __str__(self):
        return f'{self.post_name}, salary: {self.post_salary} PLN'
    
class Location(models.Model):
    location_id = models.AutoField(primary_key=True, unique=True, blank=False)
    location_street = models.CharField(max_length=255, blank=False)
    location_number = models.CharField(max_length=5, blank=False)
    location_postcode = models.CharField(max_length=6, blank=False)
    location_phone = models.CharField(max_length=9, blank=False, unique=True)

    def __str__(self):
        return f'{self.location_street}, {self.location_number}, {self.location_postcode}, phone: {self.location_phone}'

class Employee(models.Model):
    employee_email = models.CharField(max_length=100, primary_key=True, blank=False)
    employee_fname = models.CharField(max_length=50, blank=False)
    employee_lname = models.CharField(max_length=50, blank=False)
    employee_phone = models.CharField(max_length=9, blank=False)
    employee_post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=False)
    employee_location = models.ForeignKey(Location, on_delete=models.CASCADE, blank=False, default=1)

    def __str__(self):
        return f'{self.employee_fname} {self.employee_lname}, email: {self.employee_email}, phone: {self.employee_phone} | post: {self.employee_post} | {self.employee_location}'

class Service(models.Model):
    service_id = models.IntegerField(primary_key=True, unique=True, blank=False)
    service_name = models.CharField(max_length=50, blank=False)
    service_price = models.FloatField(default=20.00)

    def __str__(self):
        return f'{self.service_name}, price: {self.service_price} PLN'

class Record(models.Model):
    record_id = models.AutoField(primary_key=True, unique=True, blank=False)
    record_start_date = models.DateField(blank=False)
    record_deadline = models.DateField(null=True, blank=True, default='')
    record_client = models.ForeignKey(Client, on_delete=models.CASCADE)
    record_service = models.ForeignKey(Service, on_delete=models.CASCADE)
    record_location = models.ForeignKey(Location, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f'start date: {self.record_start_date}, deadline: {self.record_deadline} | {self.record_client} | {self.record_service} | {self.record_location}'
