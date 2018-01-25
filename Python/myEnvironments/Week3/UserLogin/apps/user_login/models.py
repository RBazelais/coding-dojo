from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    id = models.IntegerField
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_address = models.CharField(max_length=255)
    age = models.IntegerField
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

# Login = students/Login

# def login(request:)
#     # get user with submitted name
#     # if user exists
#         # compare passwords
#     # if not
#         # redirect

# def logout(request):
#     pass
#     request.session.clear()
#     return redirect ('/')
