from django.urls import path
from . import views

urlpatterns = [
    path ('loads', views.index),
    path('', views.index, name='index'),
]