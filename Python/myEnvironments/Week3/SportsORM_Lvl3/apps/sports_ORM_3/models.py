from __future__ import unicode_literals
from django.db import models

class League(models.Model):
    name = models.CharField(max_length=50)
    sport = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    #one to many
    # team_set() 
    # League.objects.first() 

    #def __str__(self):
    #   return self.team_name


class Team(models.Model):
    team_name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    league = models.ForeignKey(League) #1 to many

class Player(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    curr_team = models.ForeignKey(Team, related_name="curr_players")
    all_teams = models.ManyToManyField(Team, related_name="all_players")

    #_set used to cross a many to many relationship
    #filter
    #include
