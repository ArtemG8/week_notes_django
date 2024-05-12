from django import forms
from weeks_notes import settings


class DataForm(forms.Form):
    date_of_create = forms.DateField(label='Дата создания', widget=forms.DateInput,input_formats=['%d-%m-%Y'],
                                     error_messages={'required': 'Заполните поля!',
                                                     'invalid': 'Что-то пошло не так, повторите запрос.',
                                                     }, )
    task = forms.CharField(label='Ваша задача', min_length=3,
                           error_messages={'required': 'Заполните поля!',
                                           'max_length': 'Ваше имя не может быть на столько длинным!',
                                           'min_length': 'Ваше имя не может быть на столько коротким!'
                                           })
