from tastypie.resources import ModelResource
from tastypie.constants import ALL
from models import Dept, Employee, ClassRoom, Lab, Word


class DeptResource(ModelResource):

    def dehydrate_name(self, bundle):
        return "%s %s" % (bundle.data['name'].upper(), bundle.data['id'])

    class Meta:
        queryset = Dept.objects.all()
        resource_name = 'dept'
        filtering = {
            'name': ALL
        }


class EmployeeResource(ModelResource):

    class Meta:
        queryset = Employee.objects.all()
        resource_name = 'employee'
        filtering = {
            'name': ALL
        }


class ClassRoomResource(ModelResource):

    class Meta:
        queryset = ClassRoom.objects.all()
        resource_name = 'classroom'
        filtering = {
            'number': ALL
        }


class LabResource(ModelResource):

    class Meta:
        queryset = Lab.objects.all()
        resource_name = 'lab'
        filtering = {
            'name': ALL
        }


class WordResource(ModelResource):

    class Meta:
        queryset = Word.objects.all()
        resource_name = 'word'
        filtering = {
            'word': ALL
        }
