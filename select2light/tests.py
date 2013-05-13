from django.test import TestCase
from django.utils.datastructures import MultiValueDict
from .models import AjaxSelect2ModelChoiceField, AjaxSelect2ModelMultipleChoiceField
from .widgets import Select2MultipleWidget, AjaxSelect2Widget, AjaxSelect2MultipleWidget


class Select2MultipleWidgetTest(TestCase):

    def test_value_from_datadict(self):
        widget = Select2MultipleWidget()
        value = widget.value_from_datadict({'testing': '1'}, {}, 'testing')
        self.assertEqual(value, '1')
        value = widget.value_from_datadict(MultiValueDict({'testing': ['1', '2']}), {}, 'testing')
        self.assertEqual(value, ['1', '2'])


class AjaxSelect2ModelChoiceFieldTest(TestCase):

    def test_init(self):
        # test the presence of required arguments
        self.assertRaises(KeyError, lambda: AjaxSelect2ModelChoiceField(resource_name="r"))
        self.assertRaises(KeyError, lambda: AjaxSelect2ModelChoiceField(api_name="v1"))
        field = AjaxSelect2ModelChoiceField(resource_name="r", api_name="v1")
        # test that field widget is right one
        widget = AjaxSelect2Widget(resource_name="r", api_name="v1")
        self.assertEquals(field.widget.resource_name, widget.resource_name)
        self.assertEquals(field.widget.api_name, widget.api_name)


class AjaxSelect2ModelMultipleChoiceFieldTest(TestCase):

    def test_init(self):
        # test the presence of required arguments
        self.assertRaises(KeyError, lambda: AjaxSelect2ModelMultipleChoiceField(resource_name="r"))
        self.assertRaises(KeyError, lambda: AjaxSelect2ModelMultipleChoiceField(api_name="v1"))
        field = AjaxSelect2ModelMultipleChoiceField(resource_name="r", api_name="v1")
        # test that field widget is right one
        widget = AjaxSelect2MultipleWidget(resource_name="r", api_name="v1")
        self.assertEquals(field.widget.resource_name, widget.resource_name)
        self.assertEquals(field.widget.api_name, widget.api_name)


class AjaxSelect2WidgetTest(TestCase):

    def test_get_context(self):
        widget = AjaxSelect2Widget(resource_name="r", api_name="v1", placeholder="Tapez ici",
                                   quietMillis=4, minimumInputLength=3, minimumResultsForSearch=4,
                                   closeOnSelect=False)
        ctx = widget.get_context('testing', '1', {})
        self.assertEqual(ctx['type'], 'hidden')
        self.assertEqual(ctx['placeholder'], 'Tapez ici')
        self.assertEqual(ctx['quietMillis'], 4)
        self.assertEqual(ctx['minimumInputLength'], 3)
        self.assertEqual(ctx['minimumResultsForSearch'], 4)
        self.assertEqual(ctx['closeOnSelect'], False)


class AjaxSelect2MultipleWidgetTest(TestCase):

    urls = 'select2light.tests_urls'

    def test_get_context(self):
        widget = AjaxSelect2MultipleWidget(resource_name="r", api_name="v1")
        ctx = widget.get_context('testing', '1', {})
        self.assertEqual(ctx['multiple'], True)

    def test_value_from_datadict(self):
        widget = AjaxSelect2MultipleWidget(resource_name="r", api_name="v1")
        value = widget.value_from_datadict({'testing': '1,3,4'}, {}, 'testing')
        self.assertEqual(value, ['1', '3', '4'])  # should be MultiValueDict
        value = widget.value_from_datadict({}, {}, 'testing')
        self.assertEqual(value, '')  # not sure it shoud be '', may be None

    def test_render(self):
        widget = AjaxSelect2MultipleWidget(resource_name="r", api_name="v1")
        html_no_initial_value = widget.render('testing', '', {})
        self.assertTrue("/about/v1/r" in html_no_initial_value)
        html_with_initial_value = widget.render('testing', ['1', '3', '4'], {})
        self.assertTrue("/about/v1/r/1;3;4" in html_with_initial_value)
