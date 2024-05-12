from django.db import models


# Create your models here.

class Monday(models.Model):
    date_of_create = models.DateField()
    task = models.TextField()

    def __str__(self):
        return f'{self.date_of_create} {self.task}'


class Tuesday(models.Model):
    date_of_create = models.DateField()
    task = models.TextField()

    def __str__(self):
        return f'{self.date_of_create} {self.task}'


class Wednesday(models.Model):
    date_of_create = models.DateField()
    task = models.TextField()

    def __str__(self):
        return f'{self.date_of_create} {self.task}'

