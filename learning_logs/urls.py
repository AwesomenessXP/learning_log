"""Defines URL patterns for learning_logs"""

from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    #REMEMBER: THEY ARE AT THE SAME LEVEL!!

    #Home page
    path('index/', views.index, name='index'),

    #Test page
    path('test/', views.test, name='test'),
]