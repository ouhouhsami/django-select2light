Django-Select2Light
===================

This is a [Django](https://www.djangoproject.com/) integration of [Select2](http://ivaynberg.github.com/select2/).

The app includes Select2 driven Django Widgets, and is based on an initial work by [AppleGrew](https://github.com/applegrew)

Installation
============

1. Install `django_select2light`

        pip install django_select2light

2. Add `select2light` to your `INSTALLED_APPS` in your project settings (you must also add `floppyforms` and `tastypie`)

3. When deploying on production server, run

        python manage.py collectstatic


External Dependencies
=====================

* django
* django-floppyforms, used to create the select2 html template
* django-tastypie, used to build the ajax requests

Note: 
* This application provides a copy of jquery and a 'personal ugly hack' of select2 version 3.3.2 (see select2light/static/select2-3.3.2/select2.js initSelection: for single and multi fields)
* For this package I used django-tastypie, but we could easily use django-rest-framework, as well a django-piston.)

Usage
=====

Select2Widget
-------------

The is just a widget customization. You just replace the default widget with Select2Widget in your field.
You can seen an exemple within EmployeeForm in testapp/testmain/forms.py
You can also set it as follow:

	import floppyforms as forms
	from select2light.widgets import Select2Widget

	class FooForm(forms.Form):
		bar = forms.ModelChoiceField(queryset=Bar.objects.all(), widget=Select2Widget) 
		bazs = forms.ModelMultipleChoiceField(queryset=Bar.objects.all(), widget=Select2Widget)


Note: If you only use this widget (and not the Ajax one), you don't need to install tastypie and floppyforms.

AjaxSelect2Widget and AjaxSelect2MultipleWidget
-----------------------------------------------

Create a ModelResource for resources you would like to use with Select2 as widget. For this, you must read tastypie documentation. Here are the outlines: 

* Create a ModelResource for a Django model in a api.py file inside your app (see testapp/testmain/api.py)
* Set the urls with your API enabled (see testapp/urls.py), referencing your ModelResources.

Associate AjaxSelect2Widget to your ModelChoiceField or AjaxSelect2MultipleWidget to your ModelMultipleChoiceField in a form. Inside your AjaxSelect2Widget or AjaxSelect2MultipleWidget you must set `resource_name` and `api_name` value to the one set in your related tastypie configuration. `resource_name` is the value set in your ModelResource (see testapp/testmain/api.py), and `api_name` is the value of your api, set in your urls.py (see testapp/urls.py).


Example Application
===================

Please see `testapp` application. 
This application is used to manually test the functionalities of this package. This also serves as a good starting point example.

You can test django-select2light using github repository (also you should consider using virtualenv and virtualenvwrapper)

	mkvirtualenv django-select2light-test
	git clone https://github.com/ouhouhsami/django-select2light.git
	cd django-select2light
	pip install -r requirements.txt
	add2virtualenv select2light
	cd testapp
	python manage.py syncdb
	python manage.py runserver

then go to http://127.0.0.1:8000/ !

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
