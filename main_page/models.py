from django.db import models


# Create your models here.


class Todo(models.Model):
    day = models.CharField('День недели', max_length=100, blank=True)
    title = models.CharField('Имя задачи', max_length=250)
    description = models.TextField('Описание задачи', blank=True)
    is_complete = models.BooleanField('Завершено или нет', default=False)
    date_of_task = models.DateField(default='2001-01-01')

    # class Meta:
    #     ordering = ['pk']

    def __str__(self):
        return f'Date: {self.date_of_task}, Title: {self.title},  Complete: {self.is_complete}'
