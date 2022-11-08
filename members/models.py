from django.db import models
from django.contrib.auth.models import User
# Create your models here.\

class Members(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length= 255)

class Order(models.Model):
    title = models.CharField(max_length=100)
    descrip = models.CharField(max_length=255)
    created = models.DateField( default=None)
    price = models.FloatField()

