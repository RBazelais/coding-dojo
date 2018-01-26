# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.forms import ModelForm

# User.objects.create("Bob", "Belcher", "bob@burgers.com", "password")

# replaces daefualt model manager
class UserManager(models.Manager):
    def basic_validator(self, post_data):
		errors = {}
		if len(post_data['first_name']) < 2:
			errors['first_name'] = "Your first ame should be more than 5 characters"
		if len(post_data['last_name']) < 2:
			errors['last_name'] = "Your last name should be more than 5 characters"
		if len(post_data['email']) < 8:
			errors['email'] = "Email should be more than 8 characters"
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
		return self.first_name