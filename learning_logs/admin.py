from django.contrib import admin

from .models import Topic, Entry, Pizzeria, Pizza

# Register your models here.
admin.site.register(Topic)
admin.site.register(Entry)
admin.site.register(Pizzeria)
admin.site.register(Pizza)