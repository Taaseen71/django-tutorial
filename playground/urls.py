# 19: import path from django.urls
# 20:  Import views module from same folder. to grab the functions
from django.urls import path
from . import views 

# 21: Name this all lower case. django searches for this specific variable.

# URLConf -> Url Configuration Module
urlpatterns = [
    #22: path() function has multiple parameters
    #22: parameter1===> route: str
    #22: parameter2===> view: (function that returns an http object) (arguments: any) -> HttpResponseBase
    #22: parameter2===> view: don't pass function, just refer to it. No function_name(), just 
    #22: path('url_endpoint', 'views.function_name')
    
    #26: change 'playground/hello/' to 'hello';
    #26: path('playground/hello/', views.say_hello)
    path('hello/', views.say_hello)
    #23: go to ../storefront/urls.py and specify this url.py needs to be called when url starts with '/playground'
    
    #27: open browser and go to 'localhosturl'/playground/hello. it will show hello world
    #28: create new folder in /playground called templates
    #28: create new html file inside /templates ==> hello.html --> next ---> views.py
]

