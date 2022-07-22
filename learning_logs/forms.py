from django import forms
from learning_logs.models import Entry, Pizzeria, Topic, Pizza

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

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': 'Entry'}

        # 'widgets' is an html form (ex: text-box, multi-line text area, drop-down)
        widgets = {'text':forms.Textarea(attrs={'cols':80})}

class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ['name']
        labels = {'name':'Pizza'}
        widgets = {'name':forms.CharField(max_length='', required=False)}