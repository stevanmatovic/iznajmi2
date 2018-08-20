from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50,unique=True)

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=2000)
    #user = models.ForeignKey(User, on_delete=models.CASCADE)

class Exchange(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=2000)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)