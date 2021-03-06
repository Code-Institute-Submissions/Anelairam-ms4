from django.test import TestCase
from .form import addItemForm


class test_addItemForm(TestCase):

    # Test of the Add Item form
    def test_item_title_is_required(self):
        form = addItemForm({'title': ''})
        self.assertFalse(form.is_valid())

    def test_item_components_is_required(self):
        form = addItemForm({'components': ''})
        self.assertFalse(form.is_valid())

    def test_item_price_is_required(self):
        form = addItemForm({'price': ''})
        self.assertFalse(form.is_valid())

    def test_item_category_is_required(self):
        form = addItemForm({'item_category': ''})
        self.assertFalse(form.is_valid())
