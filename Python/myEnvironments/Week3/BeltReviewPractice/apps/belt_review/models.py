from __future__ import unicode_literals
from django.db import models

# Create your models here.
class NewUser(models.Model):
    name = models.CharField(max_length = 254)
    alias = models.CharField(max_length = 254)
    email = models.EmailField(max_length = 254)
    password = models.CharField(max_length =50)
    confirm_password = models.CharField(max_length =50)
    
# class User(models.Model):
#     email = models.EmailField(max_length = 254)
#     password = models.CharField(max_length =50)