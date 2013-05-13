from django.contrib import admin
import floppyforms as forms
from django.db import models
from select2light.widgets import Select2Widget, Select2MultipleWidget, AjaxSelect2Widget, AjaxSelect2MultipleWidget
from .models import ClassRoom, Lab, Dept, Employee, Word


class EmployeeAdminForm(forms.ModelForm):
    """
    Employee Admin Form used in EmployeeAdmin
    """
    class Meta:
        model = Employee
        widgets = {
            # Below we set up an AjaxSelect2Widget for dept field
            'dept': AjaxSelect2Widget(resource_name="dept", api_name="v1"),
        }


class EmployeeAdmin(admin.ModelAdmin):
    """
    EmployeeAdmin
    """
    form = EmployeeAdminForm
    formfield_overrides = {
        # Below we override all ForeignKey, width Select2Widget widget (no Ajax)
        models.ForeignKey: {'widget': Select2Widget},
    }


class DeptAdminForm(forms.ModelForm):
    """
    Dept Admin Form used in EmployeeAdmin
    """
    class Meta:
        model = Dept
        widgets = {
            # Below we set up an AjaxSelect2MultipleWidget for allotted_labs field
            'allotted_labs': AjaxSelect2MultipleWidget(resource_name="lab", api_name="v1"),
        }


class DeptAdmin(admin.ModelAdmin):
    """
    DeptAdmin
    """
    form = DeptAdminForm
    formfield_overrides = {
        # Below we override all ManyToManyField, width Select2MultipleWidget widget (no Ajax)
        models.ManyToManyField: {'widget': Select2MultipleWidget},
    }

admin.site.register(ClassRoom)
admin.site.register(Lab)
admin.site.register(Dept, DeptAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Word)
