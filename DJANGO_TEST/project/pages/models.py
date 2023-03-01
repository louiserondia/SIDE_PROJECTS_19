from django.db import models
from django.utils import timezone
from datetime import date

# Create your models here.

@property
class Event(models.Model):	
	date = models.DateTimeField(default=timezone.now)
	drinks = models.CharField(max_length = 2)
	name = models.CharField(max_length = 100)
	duration = models.IntegerField()

	def	is_current(self):
		return date.today() > self.date
		

class Participant(models.Model):
	participant = models.CharField(max_length = 100)

class Scan(models.Model):
	uid = models.CharField(max_length=15)
	date = models.DateTimeField(default=timezone.now)

