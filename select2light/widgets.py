from django.utils.encoding import force_text
from django.utils.datastructures import MultiValueDict, MergeDict
import floppyforms as forms


class Select2Widget(forms.Select):
    """
    Select2Widget
    Simple Select2 widget integration, no ajax request
    """
    template_name = 'select2light/select2.html'

    class Media:
        js = ('jquery-1.7.2.min.js', 'select2-3.3.2/select2.js')
        css = {'all': ('select2-3.3.2/select2.css', )}


class Select2MultipleWidget(Select2Widget):
    """
    Select2MultipleWidget
    Simple Select2 multiple widget integration, no ajax request
    """
    allow_multiple_selected = True

    def value_from_datadict(self, data, files, name):
        if isinstance(data, (MultiValueDict, MergeDict)):
            return data.getlist(name)
        return data.get(name, None)


class AjaxSelect2Widget(forms.TextInput):
    """
    AjaxSelect2Widget, to be used with ModelChoiceField
    Ajax Select2 widget, with ajax requests
    """
    template_name = 'select2light/ajax_select2.html'

    def __init__(self, *args, **kwargs):
        self.resource_name = kwargs.pop('resource_name')
        self.api_name = kwargs.pop('api_name')
        self.label_key = kwargs.pop('label_key', 'name')
        # Attribute names come from JavaScript.
        # They follow javascript naming conventions,
        # so they don't always follow PEP.
        self.placeholder = kwargs.pop('placeholder', 'Input')
        self.quietMillis = kwargs.pop('quietMillis', 100)
        self.minimumInputLength = kwargs.pop('minimumInputLength', 2)
        self.minimumResultsForSearch = kwargs.pop('minimumResultsForSearch', 6)
        self.closeOnSelect = kwargs.pop('closeOnSelect', True)
        super(AjaxSelect2Widget, self).__init__(*args, **kwargs)

    def get_context(self, name, value, attrs):
        ctx = super(AjaxSelect2Widget, self).get_context(name, value, attrs)
        ctx.update({
            'placeholder': self.placeholder,
            'quietMillis': self.quietMillis,
            'minimumInputLength': self.minimumInputLength,
            'minimumResultsForSearch': self.minimumResultsForSearch,
            'closeOnSelect': self.closeOnSelect,
            'multiple': False,
            'label_key': self.label_key,
            'resource_name': self.resource_name,
            'api_name': self.api_name
        })
        ctx['type'] = 'hidden'
        return ctx

    class Media:
        js = ('jquery-1.7.2.min.js', 'select2-3.3.2/select2.js')
        css = {'all': ('select2-3.3.2/select2.css', )}


class AjaxSelect2MultipleWidget(AjaxSelect2Widget):
    """
    AjaxSelect2MultipleWidget, to be used with ModelMultipleChoiceField
    Ajax Select2 widget, with ajax requests
    """
    pk_list = ''

    def render(self, name, value, attrs=None):
        '''
        Here is the 'messy part'
        For select multiple fields, we need to convert the value
        of the field, which is a MultiDict,
        to a format that will be set inside an Input field.
        And if value is not empty, this value will be needed
        to init the select2 javascript part of the widget with current values.
        This render method is called before get_context one, so we set
        our pk_list attribute to feet our needs.
        The pk_list is used to build the url to get the current values
        in the javascript part of the widget.
        '''
        if value:
            value = ','.join([force_text(v) for v in value])
            self.pk_list = value.replace(',', ';')
        else:
            value = ''
            self.pk_list = ''
        return super(AjaxSelect2MultipleWidget, self).render(name, value, attrs)

    def get_context(self, name, value, attrs):
        ctx = super(AjaxSelect2MultipleWidget, self).get_context(name, value, attrs)
        ctx.update({
            'multiple': True,
            'pk_list': self.pk_list  # see above for explanations
        })
        return ctx

    def value_from_datadict(self, data, files, name):
        value = data.get(name)
        if value:
            return value.split(',')
        else:
            return ''  # not sure, None could be more appropriate
