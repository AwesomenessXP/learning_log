"""learning_log URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # these are two different views when you enter the website:
    # REMEMBER: they are at the same level!!

    path('admin/', admin.site.urls), # http://127.0.0.1:8000/admin/  

    # this path uses '' AND it can chain other urls from include()  
    # REMEMBER: include () chains other urls
    path('', include('learning_logs.urls')), # http://127.0.0.1:8000/main/
]
