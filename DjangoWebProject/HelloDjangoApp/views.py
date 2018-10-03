from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


# Create your views here.
def index(request) :
    now = datetime.now()
    
    return render(
        request,
        'index.html', # Relative path from the 'templates' folder to the template file
        {
            'title':'Django',
            'message':'Hello Django!',
            'content': now.strftime("%A, %d %B, %Y at %X")    
        }
    )

def home(request) :
    return HttpResponse("Hello, home!")

def about(request) :
    return render(
        request,
        'about.html',
        {
         'title':'About HelloDjangoApp',
         'content':'Sample page for Django.'
        }
    )
