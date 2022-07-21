from django import forms
from learning_logs.models import Pizzeria, Topic

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic 
        fields = ['text']
        label = {'text':''}

class PizzeriaForm(forms.ModelForm):
    class Meta:
        model = Pizzeria
        fields = ['name']
        label = {'name':''}
    