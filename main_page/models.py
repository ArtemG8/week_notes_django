from django.db import models


# Create your models here.


class Todo(models.Model):
    day = models.CharField('День недели', max_length=100, blank=True)
    title = models.CharField('Имя задачи', max_length=500)
    is_complete = models.BooleanField('Завершено', default=False)
    date_of_task = models.DateField(default='2001-01-01')

    def __str__(self):
        return f'Date: {self.date_of_task}, Title: {self.title},  Complete: {self.is_complete}'

# class Monday(models.Model):
#     date_of_create = models.DateField()
#     task = models.TextField()
#
#     def __str__(self):
#         return f'{self.date_of_create} {self.task}'
#
#
# class Tuesday(models.Model):
#     date_of_create = models.DateField()
#     task = models.TextField()
#
#     def __str__(self):
#         return f'{self.date_of_create} {self.task}'
#
#
# class Wednesday(models.Model):
#     date_of_create = models.DateField()
#     task = models.TextField()
#
#     def __str__(self):
#         return f'{self.date_of_create} {self.task}'
