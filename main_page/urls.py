from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main),
    path('info/<str:sign_day>/', views.info_ab_days, name='info_dir'),
    path('form', views.Form, name='form_dir')
]