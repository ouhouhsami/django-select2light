from django.conf.urls import *
from django.views.generic import TemplateView
from tastypie.api import Api
from testmain.api import DeptResource, EmployeeResource, ClassRoomResource, LabResource, WordResource

v1_api = Api(api_name='v1')
v1_api.register(DeptResource())
v1_api.register(EmployeeResource())
v1_api.register(ClassRoomResource())
v1_api.register(LabResource())
v1_api.register(WordResource())

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name="index.html"), name='home'),
    url(r'^test/', include('testapp.testmain.urls')),
    (r'^api/', include(v1_api.urls)),
)
