
from .models import Employee, Dept, ClassRoom, Word

import floppyforms as forms
from select2light.widgets import Select2Widget, AjaxSelect2Widget, AjaxSelect2MultipleWidget


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
            'allotted_rooms': AjaxSelect2MultipleWidget(resource_name='classroom', api_name='v1', label_key="number"),
            'allotted_labs': AjaxSelect2MultipleWidget(resource_name='lab', api_name='v1')
        }


class MixedForm(forms.Form):
    emp1 = forms.ModelChoiceField(queryset=Employee.objects.all(),
                                  widget=AjaxSelect2Widget(resource_name='employee', api_name='v1'))
    rooms1 = forms.ModelChoiceField(queryset=ClassRoom.objects.all(),
                                    widget=AjaxSelect2Widget(resource_name='classroom', api_name='v1',
                                                             label_key="number"))
    emp2 = forms.ModelChoiceField(queryset=Employee.objects.all(),
                                  widget=AjaxSelect2Widget(resource_name='employee', api_name='v1'))
    rooms2 = forms.ModelChoiceField(queryset=ClassRoom.objects.all(),
                                    widget=AjaxSelect2Widget(resource_name='classroom', api_name='v1'))
    rooms3 = forms.ModelChoiceField(queryset=ClassRoom.objects.all(),
                                    widget=AjaxSelect2Widget(resource_name='classroom', api_name='v1'))
    any_word = forms.ModelChoiceField(queryset=Word.objects.all(),
                                      widget=AjaxSelect2Widget(resource_name='word', api_name='v1',
                                                               label_key="word"))
