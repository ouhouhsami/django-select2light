from floppyforms.models import ModelChoiceField, ModelMultipleChoiceField
from .widgets import Select2Widget, Select2MultipleWidget, AjaxSelect2Widget, AjaxSelect2MultipleWidget


class Select2ModelChoiceField(ModelChoiceField):
    """
    Select2ModelChoiceField
    Field which use Select2Widget as widget rendering
    Basic use of Select2, no Ajax inside
    """
    widget = Select2Widget


class Select2ModelMultipleChoiceField(ModelMultipleChoiceField):
    """
    Select2ModelMultipleChoiceField
    Field which use Select2MultipleWidget as widget rendering
    Basic use of Select2, no Ajax inside
    """
    widget = Select2MultipleWidget


class AjaxSelect2ModelChoiceField(ModelChoiceField):
    """
    AjaxSelect2ModelChoiceField
    Field which use AjaxSelect2Widget as widget rendering
    Use Select2 with Ajax calls for datas
    """

    def __init__(self, *args, **kwargs):
        if 'resource_name' not in kwargs:
            raise KeyError("AjaxSelect2ModelChoiceField must define a 'resource_name' key argument")
        if 'api_name' not in kwargs:
            raise KeyError("AjaxSelect2ModelChoiceField must define a 'api_name' key argument")
        self.resource_name = kwargs.pop('resource_name')
        self.api_name = kwargs.pop('api_name')
        self.label_key = kwargs.pop('label_key', 'name')
        self.widget = AjaxSelect2Widget(resource_name=self.resource_name, api_name=self.api_name, label_key=self.label_key)
        field = super(AjaxSelect2ModelChoiceField, self).__init__(args, kwargs)
        return field


class AjaxSelect2ModelMultipleChoiceField(ModelMultipleChoiceField):
    """
    AjaxSelect2ModelMultipleChoiceField
    Field which use AjaxSelect2MultipleWidget as widget rendering
    Use Select2 with Ajax calls for datas
    """

    def __init__(self, *args, **kwargs):
        if 'resource_name' not in kwargs:
            raise KeyError("AjaxSelect2ModelMultipleChoiceField must define a 'resource_name' key argument")
        if 'api_name' not in kwargs:
            raise KeyError("AjaxSelect2ModelMultipleChoiceField must define a 'api_name' key argument")
        self.resource_name = kwargs.pop('resource_name')
        self.api_name = kwargs.pop('api_name')
        self.label_key = kwargs.pop('label_key', 'name')
        self.widget = AjaxSelect2MultipleWidget(resource_name=self.resource_name, api_name=self.api_name, label_key=self.label_key)
        field = super(AjaxSelect2ModelMultipleChoiceField, self).__init__(args, kwargs)
        return field
