
from .models import Employee, Dept, ClassRoom, Word

import floppyforms as forms
from select2light.widgets import Select2Widget, Select2MultipleWidget, AjaxSelect2Widget, AjaxSelect2MultipleWidget
from select2light.models import Select2ModelChoiceField, Select2ModelMultipleChoiceField, AjaxSelect2ModelChoiceField, AjaxSelect2ModelMultipleChoiceField


class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        widgets = {
            'dept': Select2Widget,  # Simple Select2 widget
            'manager': AjaxSelect2Widget(resource_name='employee', api_name='v1')  # Ajax Select2 widget
        }


class DeptForm(forms.ModelForm):

    class Meta:
        model = Dept
        widgets = {
            'allotted_rooms': Select2MultipleWidget,
            'allotted_labs': AjaxSelect2MultipleWidget(resource_name='lab', api_name='v1')
        }


class MixedForm(forms.Form):
    emp1 = Select2ModelChoiceField(queryset=Employee.objects.all())
    rooms1 = AjaxSelect2ModelChoiceField(queryset=ClassRoom.objects.all(), resource_name='classroom', api_name='v1', label_key='number')
    emp2 = AjaxSelect2ModelChoiceField(queryset=Employee.objects.all(), resource_name='employee', api_name='v1')
    rooms2 = AjaxSelect2ModelChoiceField(queryset=ClassRoom.objects.all(), resource_name='classroom', api_name='v1', label_key='number')
    rooms3 = AjaxSelect2ModelChoiceField(queryset=ClassRoom.objects.all(), resource_name='classroom', api_name='v1', label_key='number')
    any_word = AjaxSelect2ModelMultipleChoiceField(queryset=Word.objects.all(), resource_name='word', api_name='v1', label_key='word')
