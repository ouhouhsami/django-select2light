Django-Select2Light
===================

This is a [Django](https://www.djangoproject.com/) integration of [Select2](http://ivaynberg.github.com/select2/).

The app includes Select2 driven Django Widgets, and is based on an initial work by [AppleGrew](https://github.com/applegrew)

Installation
============

1. Install `django_select2light`

        pip install django_select2light

2. Add `select2light` to your `INSTALLED_APPS` in your project settings.

3. When deploying on production server, run

        python manage.py collectstatic


External Dependencies
=====================

* Django - This is obvious.
* django-floppyforms, used to create the select2 html template
* django-tastypie, used to build the ajax requests
* jQuery


Usage
=====

* Create a ModelResource for resources you would like to use Select2 as widget. For this, you should read the tastypie documentation (tastypie in INSTALLED_APPS, create the ModelResource in api.py, set the urls with your API enabled)
* Create a form, and set the widget you want to use on ModelChoiceField or ModelMultipleChoiceField. For Ajax Widget, you must set the related tastypie keys: resource_name and api_name. 


Example Application
===================

Please see `testapp` application. 
This application is used to manually test the functionalities of this package. This also serves as a good starting point example.

You can test django-select2light using github repository (also you should consider using virtualenv and virtualenvwrapper)
* mkvirtualenv django-select2light-test
* git clone https://github.com/ouhouhsami/django-select2light.git
* cd django-select2light
* pip install -r requirements.txt
* add2virtualenv select2light
* cd testapp
* python manage.py syncdb
* python manage.py runserver
* go to http://127.0.0.1:8000/

You can also test this application using the tar.gz archive available on pypi.
* Download the tar.gz https://pypi.python.org/pypi/django-select2light/
* Extract it
* run 'python setup.py install'
* cd into testapp
* python manage.py syncdb
* python manage.py runserver
* go to http://127.0.0.1:8000/


License
=======

Copyright 2012 Samuel Goldszmidt

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this project except in compliance with the License.
You may obtain a copy of the License at

[http://www.apache.org/licenses/LICENSE-2.0](http://www.apache.org/licenses/LICENSE-2.0)

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
