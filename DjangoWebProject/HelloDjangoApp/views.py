from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


# Create your views here.
def index(request) :
    now = datetime.now()
    
    html_content = '<html><head><title>hello django test</title></head><body>'
    html_content += '<strong>datetime</strong> on ' + now.strftime('%A, %d, %B, %Y at %X')
    html_content += '</body></html>'

    return HttpResponse(html_content)

def home(request) :
    return HttpResponse("Hello, home!")
