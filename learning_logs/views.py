from django.shortcuts import render, redirect

from .models import Topic, Pizzeria
from .forms import TopicForm

# Create your views here.
# the render() funtion renders the response based on data provided by views
# render takes 2 args: request (the action), and template (index.html)

"""
HOW TO MAKE A NEW PAGE:
1. specify url pattern with path()
2. write a view function (and return the html file)
3. write a template (the html file)
4. (optional) if you need an index, use <int:index_num>
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

def topic(request, topic_id):
    """Show a single topic and all its entries"""

    # we want to access topic_id attributes from the class
    topic = Topic.objects.get(id=topic_id) #ex: 1, 2, 3

    # REMEMBER: we can access the related objects bc of 'one to many' relationship
    entries = topic.entry_set.order_by('-date_added') #ex: 7/20/22, 7/21/22

    # in context, we define a dictionary of all defined objects
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

def pizza(request):
    pizzerias = Pizzeria.objects.all() # send this data to the html page
    context = {'pizzerias': pizzerias}
    return render(request, 'learning_logs/pizzerias.html', context)

def pizzas(request, pizzeria_id):
    pizzeria = Pizzeria.objects.get(pk=pizzeria_id) # the ID (some integer) of the page depends on the pizzeria id
    toppings = pizzeria.pizza_set.all()
    context = {'toppings': toppings, 'pizzeria': pizzeria}
    return render(request, 'learning_logs/pizzas.html', context)

def new_topic(request):
    """Add a new topic"""
    # IMPORTANT:
    # 1. GET - request to read data from server
    # 2. POST - request to submit user data from a form
    if (request.method != 'POST'): # if method is GET, else method is POST
        # No data submitted? create a blank form
        form = TopicForm() # because of no argument --> makes blank form
    else:
        # POST data sumbitted -> process data
        # REMEMBER: check data is valid before saving in database
        form = TopicForm(data=request.POST)
    if (form.is_valid()):
        form.save()
        return redirect('learning_logs:topics') # go to a different page

    #Display a blank or invalid form
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)
            
