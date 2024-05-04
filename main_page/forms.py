from django import forms


class DataForm(forms.Form):
    monday = forms.CharField(label='Monday',  min_length=2,
                           error_messages={'required': 'Заполните поля!',
                                           'invalid': 'Что-то пошло не так, повторите запрос.',
                                           'max_length': 'Ваше имя не может быть на столько длинным!',
                                           'min_length': 'Ваше имя не может быть на столько коротким!'
                                           }, )
    tuesday = forms.CharField(label='Tuesday', min_length=3,
                              error_messages={'required': 'Заполните поля!',
                                              'max_length': 'Ваше имя не может быть на столько длинным!',
                                              'min_length': 'Ваше имя не может быть на столько коротким!'
                                              })
