from django.shortcuts import render
# Create your views here.

#! Started here. 
# request -> response
# request handler
# action 
# 18: import HttpResponse from django.http and create say_hello function 
from django.http import HttpResponse


def calculate():
    x = 1;
    y = 2
    return x

# 18: return HttpResponse("Hello World")
def say_hello(request):
    # return HttpResponse('Hello World')
    #  x = calculate()
    #30: return render html file. from django.shortcuts import render;
    #30: return render("type: request/response", "html_file_name", "send Dictionary / Object" )
    return render(request, 'hello.html', {'name': 'Saadat'} )
    #31: Go to notes.md for django-toolbar install

#19: Map this function to a URL. So when we hit the url, we get this function to run. 

#18: Create new file called: urls.py --> Next methods there.
#29: Change HttpResponse to hello.html