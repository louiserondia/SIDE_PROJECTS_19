from django.db import models

# Create your models here.
class Badge(models.Model):
	UID = models.CharField(max_length = 12)
	Ref = models.CharField(max_length = 4)
	