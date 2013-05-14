Django-Select2Light
===================

[![Build Status](https://travis-ci.org/ouhouhsami/django-select2light.png?branch=master)](https://travis-ci.org/ouhouhsami/django-select2light)

This is a [Django](https://www.djangoproject.com/) integration of [Select2](http://ivaynberg.github.com/select2/).

The app includes Select2 driven Django Widgets, and is based on an initial great work by [AppleGrew](https://github.com/applegrew)


Installation
============

1. Install Django_Select2Light

        pip install django_select2light

2. Add `select2light` to your `INSTALLED_APPS` in your project settings (you must also add `floppyforms` and `tastypie`)

3. When deploying on production server, run

        python manage.py collectstatic


External Dependencies
=====================

* django, as long as this is a django app ...
* django-floppyforms, used to create the select2 html templates
* django-tastypie, used to build the ajax requests

Note: 
* This application provides a copy of jquery and a 'personal ugly hack' of select2 version 3.3.2 (see select2light/static/select2-3.3.2/select2.js initSelection: for single and multi fields)
* For this package I used [django-tastypie](http://django-tastypie.readthedocs.org/en/latest/), but we could easily use [django-rest-framework](http://django-rest-framework.org/), as well a [django-piston](https://django-piston.readthedocs.org/en/latest/documentation.html))


Usage
=====

Select2Widget and Select2MultipleWidget
---------------------------------------

This is just a widget customization. Using Select2Widget or Select2MultipleWidget, you will replace the default widget with Select2Widget for your ModelChoiceField or Select2MultipleWidget for your ModelMultipleChoiceField.

You can set it as follow:

	import floppyforms as forms
	from select2light.models import Select2ModelChoiceField, Select2ModelMultipleChoiceField
	from select2light.widgets import Select2Widget, Select2MultipleWidget
	form models import Bar, Baz

	# use directly the custom field
	class FooForm(forms.Form):
		bar = Select2ModelChoiceField(queryset=Bar.objects.all()) 
		bazs = Select2ModelMultipleChoiceField(queryset=Baz.objects.all())

	# ... or just use the widget
	class FooForm(forms.Form):
		bar = forms.ModelChoiceField(queryset=Bar.objects.all(), widget=Select2Widget) 
		bazs = forms.ModelMultipleChoiceField(queryset=Baz.objects.all(), widget=Select2MultipleWidget)


You can also see an usage exemple within the `EmployeeForm` ModelForm class Meta in [forms.py](https://github.com/ouhouhsami/django-select2light/blob/master/testapp/testapp/testmain/forms.py#L13)

Note: 
* If you only use Select2Widget (and not the Ajax widgets as described below), you don't need to install tastypie nor floppyforms.
* If you want to set specific params to the Select2 instanciation (see list in Constructor part of this page http://ivaynberg.github.io/select2/), for this case, you need to override the default select2light/select2.html template. Depending on user needs, we could consider, as below for the Ajax widgets, having some instantiations params that would configure select2 widget.


AjaxSelect2Widget and AjaxSelect2MultipleWidget
-----------------------------------------------

### django-tastypie part

Create a ModelResource for resources (in most cases, Django models) you would like to use with Select2 as widget. For this, you must read [django-tastypie](http://django-tastypie.readthedocs.org/en/latest/) documentation. Here are the outlines: 

Create a ModelResource for a Django model in `api.py` file inside your app (see [api.py](https://github.com/ouhouhsami/django-select2light/blob/master/testapp/testapp/testmain/api.py))

	# api.py file
	from tastypie.resources import ModelResource
	from tastypie.constants import ALL
	from models import Bar

	class BarResource(ModelResource):

    	class Meta:
        	queryset = Bar.objects.all()
        	resource_name = 'bar'
        	filtering = {
            	'name': ALL  # assuming Bar has a field named name
        	}


Set the urls with your API enabled (see [urls.py](https://github.com/ouhouhsami/django-select2light/blob/master/testapp/testapp/urls.py)), referencing your ModelResources.

	# urls.py file
	from django.conf.urls import *
	from tastypie.api import Api
	from myapp.api import BarResource

	foo_api = Api(api_name='foobar')
	foo_api.register(BarResource())

	# ... your urlpatterns

	urlpatterns += patterns('',
       (r'^api/', include(foo_api.urls)),
    )
	

### select2light part

Associate `AjaxSelect2Widget` to your `ModelChoiceField` (or `AjaxSelect2MultipleWidget` to your `ModelMultipleChoiceField`) in a Form class. 
Inside `AjaxSelect2Widget` (or `AjaxSelect2MultipleWidget`) you configure the following params: 
* `resource_name` (required) is the value set in your tastypie ModelResource (see example [api.py](https://github.com/ouhouhsami/django-select2light/blob/master/testapp/testapp/testmain/api.py#L14))
* `api_name` (required) is the value of your api, set in your urls.py (see example [urls.py](https://github.com/ouhouhsami/django-select2light/blob/master/testapp/testapp/urls.py#L6))
* `label_key` (optional) corresponds to the field you want to search on in your ModelResource. Default is set to 'name'. There are two ways to work with it: you can add a field name `name` to your ModelResource (and [use dehydrate tastypie functionality](http://django-tastypie.readthedocs.org/en/latest/cookbook.html#adding-custom-values)) or you can set `label_key` to a custom field on your ModelResource to search by this key.

```
# forms.py file
from models import Bar
import floppyforms as forms
form select2light.models import AjaxSelect2ModelChoiceField, AjaxSelect2ModelMultipleChoiceField
form select2light.wigets import AjaxSelect2Widget, AjaxSelect2MultipleWidget

# use directly the custom field
class FooForm(form.Form):
	# assuming Bar model has a name field
	bar = AjaxSelect2ModelChoiceField(queryset=Bar.objects.all(),
	                                  resource_name='bar', api_name='foobar')
	bazs = AjaxSelect2ModelMultipleChoiceField(queryset=Baz.objects.all(),
	                                           resource_name='bar', api_name='foobar')

# ... or just use the widget
class FooForm(form.Form):
	# assuming Bar model has a name field
	bar = forms.ModelChoiceField(queryset=Bar.objects.all(),
	                             widget=AjaxSelect2Widget(resource_name='bar', api_name='foobar'))
	bazs = forms.ModelMultipleChoiceField(queryset=Baz.objects.all(),
										  widget=AjaxSelect2MultipleWidget(resource_name='baz', api_name='foobar'))
```

Note:
For ModelForm you can just override widget dict in class Meta of your ModelForm, as done in test app [forms.py](https://github.com/ouhouhsami/django-select2light/blob/master/testapp/testapp/testmain/forms.py#L15). 


Admin integration
=================

You can use the widgets or the fields in the admin. The testapp project propose different use cases, see [admin.py](https://github.com/ouhouhsami/django-select2light/blob/master/testapp/testapp/testmain/admin.py) for examples.


To go further (shared ideas)
============================

* Consider replacing Select2 with a custom HTML5 datalist implementation
* Be Rest framework agnostic, try to work with any of the Django Rest Framework mentioned above
* Remove 'Hold down "Control", or "Command" on a Mac, to select more than one.' on select multiple widget rendering.


Changelog
=========

0.3
* Add Travis CI as continuous integration service
* Add admin integration examples

0.2
* Add tests
* Add fields Select2ModelChoiceField, Select2ModelMultipleChoiceField, AjaxSelect2ModelChoiceField, AjaxSelect2ModelMultipleChoiceField for convenience
* Update README

0.1
* First release to test the feasibility, using base structuration proposed by [AppleGrew](https://github.com/applegrew)


Example Application
===================

Please see `testapp` application. 
This application is used to manually test the functionalities of this package. This also serves as a good starting point example.

You can test django-select2light using github repository (also you should consider using virtualenv and virtualenvwrapper)

	mkvirtualenv django-select2light-test
	git clone https://github.com/ouhouhsami/django-select2light.git
	cd django-select2light
	pip install -r requirements.txt
	pip install -r requirements-tests.txt
	add2virtualenv select2light
	cd testapp
	python manage.py syncdb
	python manage.py runserver

Then go to http://127.0.0.1:8000/ !


You can also test this application using the tar.gz archive available on pypi.

	Download the tar.gz https://pypi.python.org/pypi/django-select2light/
	Extract it
	run 'python setup.py install'
	install converage and django-coverage
	cd into testapp
	python manage.py syncdb
	python manage.py runserver
	go to http://127.0.0.1:8000/


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
