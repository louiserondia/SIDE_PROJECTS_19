from django.db import models
from users.models import User

# Create your models here.
class Ownership(models.Model):
	user = models.CharField(max_length = 100)
	badge = models.CharField(max_length = 100)
	date_init = models.DateTimeField(auto_now_add=False)
	date_event_in = models.DateTimeField(auto_now=False)