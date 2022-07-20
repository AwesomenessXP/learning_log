from django.db import models

# Create your models here.
class Topic(models.Model):
    """A topic the user is learning about"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self): # returns a string of Topic.text
        """ Return a string representation of the model """
        return self.text

class Entry(models.Model):
    """Something specific learned about a topic"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)

# this class holds extra information about the model
# and tells Django to use Entries to refer to more than one entry
    class Meta: 
        verbose_name_plural = 'entries'

    def __str__(self):
        """Return a string representation of the model"""
        return f"{self.text[:50]}" #show only the first 50 characters

class Pizzeria(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name[:50]}"

class Topping(models.Model):
    pizza = models.ForeignKey(Pizzeria, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name[:50]}"