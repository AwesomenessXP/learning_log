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
    path('pizzerias/', views.pizza, name='pizzerias'),

    # Detail page for a single topic
    # 'topics' tells Django to look for URL with 'topics' after base URL
    # <int:topic_id> matches an integer that stores the integer in topic_d
    path('topics/<int:topic_id>/', views.topic, name='topic'),

    # Topping
    path('pizzerias/<int:pizzeria_id>/', views.pizzas, name='pizza') # simple mistake here, DONT FORGET BRACKETS!!
]