from django.contrib import admin
from django.db import models
from select2light.widgets import Select2Widget, Select2MultipleWidget
from .models import ClassRoom, Lab, Dept, Employee, Word


class EmployeeAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ForeignKey: {'widget': Select2Widget},
    }


class DeptAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ManyToManyField: {'widget': Select2MultipleWidget},
    }

admin.site.register(ClassRoom)
admin.site.register(Lab)
admin.site.register(Dept, DeptAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Word)
