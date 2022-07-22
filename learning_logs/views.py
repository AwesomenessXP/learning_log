from django.shortcuts import render, redirect

from .models import Topic, Pizzeria, Entry, Pizza
from .forms import TopicForm, PizzeriaForm, EntryForm, PizzaForm

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
    # 3. this function shows basic form validation

    # if method is GET, else method is POST
    if (request.method != 'POST'): 
        # No data submitted? create a blank form
        form = TopicForm() # because of no argument --> makes blank form
    else:
        # POST data sumbitted -> process data
        # REMEMBER: check data is valid before saving in database
        form = TopicForm(data=request.POST)

    # if valid, redirect to topics, else -> display blank form
    if (form.is_valid()):
        form.save()

        # home -> topic page -> click on 'add topic' -> new_topic page -> original topic page with new item
        return redirect('learning_logs:topics') # go back to page where topics are listed

    #Display a blank or invalid form
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

def new_pizzeria(request):
    if (request.method != 'POST'):
        form = PizzeriaForm() # make a blank form if nothing to send to server
    else:
        form = PizzeriaForm(data=request.POST)
    
    if (form.is_valid()):
        form.save()

        # home -> pizzeria page -> click on 'add pizzeria' -> new_pizzeria page -> original pizzeria page with new item
        return redirect('learning_logs:pizzerias') # go back to page where pizzerias are listed  

    context = {'form':form}  
    return render(request, 'learning_logs/new_pizzeria.html', context) 

def new_entry(request, topic_id):
    """Add a new entry for a particular topic"""
    topic = Topic.objects.get(id=topic_id)

    # validate requests in form
    if (request.method != 'POST'):
        form = EntryForm() # no data submitted? create a blank form
    else:
        form = EntryForm(data=request.POST)
    
        # return response based on request
        if (form.is_valid()):
            # commit=False means make a new entry object without saving it to the database
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)

    # Display a blank or invalid form
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html',context)

def new_pizza(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id) # get id for pizza objects, will use them to return later

    if (request.method != 'POST'):
        form = PizzaForm()
    else:
        form = PizzaForm(data=request.POST)
        if form.is_valid():
            new_pizza = form.save(commit=False)
            new_pizza.pizza = pizza
            new_pizza.save()
            return redirect('learning_logs:pizza', pizza_id=pizza_id)

    context = {'pizza':pizza, 'form': form}
    return render(request, 'learning_logs/new_pizza.html', context)

def edit_entry(request, entry_id):
    # when edit_entry recieves a GET request, edit_entry() returns a form for editing
    """Edit an existing entry"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if (request.method != 'POST'):
        # initial request: pre-fill form with current entry
        # create a form instance based on existing entry object!!
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)

        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)
    
    context = {'entry': entry, 'topic':topic, 'form':form}
    return render(request, 'learning_logs/edit_entry.html', context)

# def edit_pizza(request, pizza_id):
#     entry = Pizza.objects.get(id=pizza_id) # create a form instance based on existing object
#     pizza = entry.pizza # get the parent (we'll display as output)

#     if (request.method != 'POST'):
#         form = PizzaForm(instance=pizza)
#     else:
#         form = PizzaForm(instance=pizza, data=request.POST)

#         if (form.is_valid()):
#             form.save()
#             return redirect('learning_logs:pizza', pizza_id=pizza.id)

#     context = {'pizza':pizza, 'entry':entry, 'form': form}
#     return render(request, 'learning_logs/edit_pizza.html', context)
