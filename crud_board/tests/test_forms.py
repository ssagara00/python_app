from django.test import TestCase

from crud_board.forms import UserForm


class TestsForms(TestCase):

    def test_userform_test(self):
        form_data = {"name": "tarou", "email": "1@gmail.com"}
        form = UserForm(form_data)
        self.assertTrue(form.is_valid())
