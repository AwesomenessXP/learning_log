from django.shortcuts import render

# Create your views here.
# the render() funtion renders the response based on data provided by views
# render takes 2 args: request (the action), and template (index.html)

# when URL request matches the pattern, Django looks for 'request' object 
def index(request):
    """The home page for Learning Log"""
    return render(request, 'learning_logs/index.html')

def test(request):
    return render(request, 'learning_logs/another.html')