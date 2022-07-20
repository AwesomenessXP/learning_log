from django.shortcuts import render

from .models import Topic, Topping

# Create your views here.
# the render() funtion renders the response based on data provided by views
# render takes 2 args: request (the action), and template (index.html)

"""
HOW TO MAKE A NEW PAGE:
1. specify url pattern
2. write a view function (and return the html file)
3. write a template (the html file)
"""

""" when URL request matches the pattern, Django looks for 'request' object 
    and also the html file
"""
def index(request):
    """The home page for Learning Log"""
    # when called, returns contents of index.html
    return render(request, 'learning_logs/index.html')

def test(request):
    # when called, returns contents of another.hmtl
    return render(request, 'learning_logs/another.html')

def silly(request):
    # when called, returns contents of silly.html
    return render(request, 'learning_logs/silly.html')

def topics(request):
    """Show all topics"""

    # query the database -> ask for Topic objects sorted by 'date_added'
    topics = Topic.objects.order_by('date_added')

    # create a dictionary that we'll use to ACCESS DATA
    context = {'topics':topics}
    return render(request, 'learning_logs/topics.html', context)

def pizza(request):
    toppings = Topping.objects.all() # send this data to the html page
    context = {'toppings': toppings}
    return render(request, 'learning_logs/toppings.html', context)