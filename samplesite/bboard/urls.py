from django.urls import path
from . import views

app_name = 'bboard'

urlpatterns = [
    path('', views.index),
]