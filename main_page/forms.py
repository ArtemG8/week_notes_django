from django import forms
from datetime import datetime
from .models import Todo


class AllData(forms.Form):
    pass


class DataForm(forms.Form):
    min_day_value = datetime.today().strftime('%Y-%m-%d')
    # date_of_create = forms.DateField(label='Дата создания', widget=forms.DateInput(
    #     attrs={'type': 'date', 'min': min_day_value, 'value': min_day_value, 'style': 'width: 200px; height: 40px;'}),
    #
    #                                  error_messages={'required': 'Заполните поля!',
    #                                                  'invalid': 'Что-то пошло не так, повторите запрос.',
    #                                                  }, )
    title = forms.CharField(label='Ваша задача', min_length=3,
                            error_messages={'required': 'Заполните поля!',
                                            'max_length': 'Ваше имя не может быть на столько длинным!',
                                            'min_length': 'Ваше имя не может быть на столько коротким!'
                                            })
    date_of_task = forms.DateTimeField(label='Выберите день задачи', error_messages={'required': 'Заполните поля!'},
                                   widget=forms.DateInput(attrs={'type': 'date'}))


# attrs={'type': 'date', 'min': min_day_value, 'value': min_day_value, 'style': 'width: 200px; height: 40px;'}),

# date_of_create = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'min': '2024-05-13'}))

# input_formats=['%d-%m-%Y'],
