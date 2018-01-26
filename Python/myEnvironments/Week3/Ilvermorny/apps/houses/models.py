# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import random

# creates Database Model
class Base(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class House(Base):
	name = models.CharField(max_length=20)
	# whenever I call house in the shell return its name instead of just house object
	def __str__(self):
		return self.name

class StudentManager(models.Manager):
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

class Student(Base):
	name = models.CharField(max_length=20)
	cult = models.ForeignKey(House, related_name="peeps")
	objects = StudentManager()
	def __str__(self):
		return self.name

class Course(Base):
	title = models.CharField(max_length=254)
	description = models.TextField(default="A Class")
	members = models.ManyToManyField(Student)

	def __str__(self):
		return self.title

def build_houses():
	houses = ['Thunder Bird', 'Wampus', 'Horned Serpent', 'Pukwudgie']
	for house in houses:
		neo = House(name=house)
		neo.save()

def generate_students():
	names = [
		'Alan',
		'Brian',
		'Robb',
		'Flo Jo',
		'Mags',
		'Chris',
		'Rachel',
		'Scott',
		'Tyler',
		'Barry',
		'Matt',

	]
	
	houses = House.objects.all()
	for n in names:
		neo = Student(name=n)
		h = houses[random.randint(0,3)]
		neo.cult = h
		neo.save()

# def create_courses():
# 	courses = ['Potions', 'Parsel Tongue', 'Divination', 'Flying 101']
# 	for course in course:
# 		neo = Course(title=course)
# 		neo.save()