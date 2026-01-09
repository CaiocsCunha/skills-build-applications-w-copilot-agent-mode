from djongo import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # Extend as needed
    pass

class Team(models.Model):
    name = models.CharField(max_length=100)
    members = models.ArrayReferenceField(to=User)
    created_at = models.DateTimeField(auto_now_add=True)

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    duration = models.IntegerField()  # minutes
    calories = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

class Leaderboard(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)

class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    suggestion = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
