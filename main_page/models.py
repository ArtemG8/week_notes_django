from django.db import models


# Create your models here.

class Days(models.Model):
    monday = models.TextField()
    tuesday = models.TextField()
    wednesday = models.TextField()

    def __str__(self):
        return f'{self.monday} {self.tuesday} {self.wednesday}'
