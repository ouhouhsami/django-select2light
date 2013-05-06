from django.utils.encoding import force_text
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
        super(AjaxSelect2Widget, self).__init__(*args, **kwargs)

    def get_context(self, name, value, attrs):
        ctx = super(AjaxSelect2Widget, self).get_context(name, value, attrs)
        ctx.update({
            'placeholder': 'Input',
            'quietMillis': 100,
            'minimumInputLength': 2,
            'minimumResultsForSearch': 6,
            'closeOnSelect': False,
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

    def get_context(self, name, value, attrs):
        ctx = super(AjaxSelect2MultipleWidget, self).get_context(name, value, attrs)
        ctx.update({
            'multiple': True,
            'pk_list': self.pk_list
        })
        return ctx

    def render(self, name, value, attrs=None):
        if value:
            value = ','.join([force_text(v) for v in value])
            self.pk_list = value.replace(',', ';')
        else:
            value = ''
        return super(AjaxSelect2MultipleWidget, self).render(name, value, attrs)

    def value_from_datadict(self, data, files, name):
        value = data.get(name)
        if value:
            return value.split(',')
