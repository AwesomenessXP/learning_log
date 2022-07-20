"""Defines URL patterns for learning_logs"""

from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    #REMEMBER: THEY ARE AT THE SAME LEVEL!!

    #Home page
    path('', views.index, name='index'),

    #Test page
    path('test/', views.test, name='test'),

    #Silly page
    path('silly/', views.silly, name='silly'), 

    #Topics page
    path('topics/', views.topics, name='topics'),

    #Pizza page
    path('pizza/', views.pizza, name='pizza'),
]