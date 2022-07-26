"""Defines URL patterns for learning_logs"""

from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

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

    # simple mistake here, DONT FORGET BRACKETS AND COMMAS!!
    path('pizzerias/<int:pizzeria_id>/', views.pizzas, name='pizza'), 

    # Page for adding a new topic
    path('new_topic/', views.new_topic, name='new_topic'),

    # Page for adding a new pizzeria
    path('new_pizzeria/', views.new_pizzeria, name='new_pizzeria'),

    # Page for adding a new entry
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),

    # Page for editing an entry
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),

    # Page for adding a new pizza
    path('new_pizza/<int:pizzeria_id>/', views.new_pizza, name='new_pizza'),

    # Page for editing pizza
    path('edit_pizza/<int:pizza_id>/', views.edit_pizza, name='edit_pizza'), 
]