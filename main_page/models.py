from django.db import models


# Create your models here.

class Days(models.Model):
    monday = models.TextField()
    tuesday = models.TextField()
    wednesday = models.TextField()

