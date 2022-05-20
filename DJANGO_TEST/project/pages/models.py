from django.db import models
from django.utils import timezone

# Create your models here.

class Event(models.Model):	
	date = models.DateTimeField(default=timezone.now)
	drinks = models.CharField(max_length = 2)
	name = models.CharField(max_length = 100)

class Participant(models.Model):
	participant = models.CharField(max_length = 100)

class Scan(models.Model):
	uid = models.CharField(max_length=15)
	date = models.DateTimeField(default=timezone.now)

