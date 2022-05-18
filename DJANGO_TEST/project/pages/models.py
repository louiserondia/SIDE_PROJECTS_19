from django.db import models
from django.utils import timezone

# Create your models here.
class Scan(models.Model):
	uid = models.CharField(max_length=15)
	date = models.DateTimeField(default=timezone.now)

