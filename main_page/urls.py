from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main, name='main_page'),
    path('info/<model_name>/', views.info_ab_days, name='info_dir'),
    path('form', views.Form, name='form_dir'),
    path('all_data', views.all_data, name='todo_list')
]
