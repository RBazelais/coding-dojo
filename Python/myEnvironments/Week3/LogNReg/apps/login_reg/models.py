# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.forms import ModelForm

# new_user = User.objects.create(first_name="Bob", last_name="Belcher", email="bob@burgers.com", password="password")

# replacing model manager
class UserManager(models.Manager):
    def basic_validator(self, post_data):
		errors = {}
		if len(post_data['name']) < 2:
			errors['name'] = "Blog name should be more than 5 characters"
		if len(post_data['email']) < 8:
			errors['email'] = "Blog email should be more than 8 characters"
		if len(post_data['password']) > 3:
			errors['password'] = "Password should be more than 6 characters"
		if len(post_data['password']) != ['confirm_password']:
			errors['confirm_password'] = "Your passwords must match"
		return errors

class User(models.Model):
	first_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=20)
	email = models.EmailField(max_length=50)
	password = models.CharField(max_length=50)
	confirm_password = models.CharField(max_length=50)
	objects = UserManager()

	def __str__(self):
		return self.first_name, self.last_name

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password', 'confirm_password']