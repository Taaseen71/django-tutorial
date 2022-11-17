#1: `pipenv install django`

#2: `cd to folder`

#3: `pipenv shell`

#4: to start a new project type: `django-admin startproject storefront` or `django-admin startproject storefront .`

#5: to run server : `python manage.py runserver`

#6: to find local server : `pipenv --venv`

#7: open Command Pallete: `command + shift + P`

#8: type in command pallete: `Python Interpreter --> Select Interpreter`;

#9: use pipenv --venv to find local python interpreter and copy the location. paste in Select Interpreter

#10: paste local file: and append `/bin/python`

#11: example: `/Users/st-personal/.local/share/virtualenvs/storefront-whGZYKqf/bin/python`

#12: close and reopen terminal and type `python manage.py runserver`. Make sure to restart terminal in vs code.

#13: go to `./storefront/settings.py` --> remove the line `'django.contrib.sessions'`,

#14: open new terminal and type: `python manage.py startapp playground`

#15: New Playground folder is created: Inside ---> 
        `admin.py` is the admin module, that decides how the admin interface for the app looks like
        `apps.py` configures the app. its the config file in node js.
        `models.py` configures the model classes. pulls data from the database and presents to user.
        `tests.py` write unit test.
        `views.py` request/response protocol handler.


#16: Register playground app in the storefront/settings.py module ---> INSTALLED_APPS = [
                                                                         ...INSTALLED_APPS,
                                                                add      `'playground'`
                                                                        ]


#17: Next Procedure in `./playgrounds/views.py`


#32: Install Django Debug toolbar
#32: new terminal --> `pipenv install django-debug-toolbar`  
#33: in storefront/settings.py -->   INSTALLED_APPS = [
                                        ...INSTALLED_APPS,
                                        `'debug_toolbar'`
                                    ]
                                    MIDDLEWARE = [
                                        ...MIDDLEWARE,
                                        `'debug_toolbar.middleware.DebugToolbarMiddleware'`,
                                    ]

#34: in storefront/urls.py ---> `import debug_toolbar`
    in storefront/urls.py -> 
                    urlpatterns = [
                        ...urlpatterns,
                        path('__debug__/', include(debug_toolbar.urls))
                    ]

#35: Add Internal IP ----> 
        new variable in storefront/settings.py -->  
```
                                            INTERNAL_IPS = [
                                                # ...
                                                '127.0.0.1'
                                                # ...
                                            ]
```
#35a:    refresh :8000 browser

#36: Data Modeling: ----> 


