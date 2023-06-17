from django.db import models
from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from datetime import date

from .managers import CustomUserManager

# Create your models here.

class Client(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), primary_key=True, unique=True)
    first_name = models.CharField(max_length=50, default="")
    last_name = models.CharField(max_length=50, default="")
    phone = models.CharField(max_length=9, blank=True, null=True, default="")
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "phone"]

    objects = CustomUserManager()

    class Meta:
        verbose_name_plural = "Client"

    def __str__(self):
        return self.email


class Posn(models.Model):
    name = models.CharField(max_length=50, primary_key=True, blank=False, null=False, unique=True)
    salary = models.DecimalField(max_digits=7, decimal_places=2, blank=False, null=False)

    class Meta:
        verbose_name_plural = "Position"

    def __str__(self):
        return f'{self.name}, salary: {self.salary} Euro'
    
class Location(models.Model):
    id = models.AutoField(primary_key=True, unique=True, blank=False, null=False)
    city = models.CharField(max_length=255, blank=False, null=False, default="Vancouver")
    street = models.CharField(max_length=255, blank=False, null=False)
    number = models.CharField(max_length=5, blank=False, null=False)
    postcode = models.CharField(max_length=6, blank=False, null=False)
    phone = models.CharField(max_length=9, blank=False, null=False, unique=True)

    class Meta:
        verbose_name_plural = "Location"

    def __str__(self):
        return f'{self.postcode}, {self.street} {self.number}'

class Employee(models.Model):
    email = models.CharField(max_length=100, primary_key=True, blank=False, null=False)
    first_name = models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=False, null=False)
    phone = models.CharField(max_length=9, blank=False, null=False)
    posn = models.ForeignKey(Posn, on_delete=models.PROTECT, blank=False, null=False)
    location = models.ForeignKey(Location, on_delete=models.PROTECT, blank=False, null=False, default=1)

    class Meta:
        verbose_name_plural = "Employee"

    def __str__(self):
        return f'{self.first_name} {self.last_name}, email: {self.email}, phone: {self.phone} | post: {self.posn} | {self.location}'

class Service(models.Model):
    id = models.AutoField(primary_key=True, unique=True, blank=False, null=False)
    name = models.CharField(max_length=50, blank=False, null=False)
    price = models.DecimalField(max_digits=7, decimal_places=2)

    class Meta:
        verbose_name_plural = "Service"

    def __str__(self):
        return f'{self.name}, price: {self.price} Euro'

class Record(models.Model):
    id = models.AutoField(primary_key=True, unique=True, blank=False, null=False)
    start_date = models.DateField(blank=False, null=False)
    deadline = models.DateField(blank=True, null=True, default=None)
    price = models.DecimalField(max_digits=7, decimal_places=2, blank=False, null=False)
    client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, default='')
    service = models.ForeignKey(Service, on_delete=models.PROTECT, blank=False, null=False)
    location = models.ForeignKey(Location, on_delete=models.PROTECT, blank=False, null=False)

    class Meta:
        verbose_name_plural = "Record"

    def __str__(self):
        return f'start date: {self.start_date}, deadline: {self.deadline} | {self.client} | {self.service} | {self.location}'
    
    @property
    def status(self):
        return date.today() > self.deadline
