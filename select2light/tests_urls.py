from django.conf.urls import *
from django.views.generic import TemplateView

# fake urls to test widgets, we don't need to test ajax part, normally done in select2
urlpatterns = patterns('',
                       url(r'^about/(?P<api_name>\w+)/(?P<resource_name>\w+)',
                           TemplateView.as_view(template_name="tests/test_api.html"),
                           name="api_dispatch_list"),
                       url(r'^about/(?P<api_name>\w+)/(?P<resource_name>\w+)/(?P<pk_list>\w+)',
                           TemplateView.as_view(template_name="tests/test_api.html"),
                           name="api_get_multiple"),)
