from django.shortcuts import render
from django.views import View

class Index(View):
    # research this 
    # when a user navigates to a URL you defined in your project, 
    # Django will check the method used for the request (if they're just viewing the page for the first time, 
    # this will be GET; another example is POST, which you probably heard before) 
    # and call the method of your view (HomePage) with the corresponding name, get(). 
    # If you also define a post() method, that will be called when the user requests the page with a POST method, 
    # for example by submitting a form with the method="post".
    # about your first question: request is an HTTP request object that is passed to the function 
    # to basically tell them what the user('s browser) has requested, what it wants to do. 
    # *args is a list of all other positional arguments that might have been added to the get() call. 
    # The same states for **kwargs, which is instead a dictionary of keyword arguments.
    #  These can very well be empty, but it's good that we pass them on to the upper level 
    # so that we don't loose any functionality that may be needed.
    
    def get(self, request, *args, **kwargs):
        return render(request, 'landing/index.html')

