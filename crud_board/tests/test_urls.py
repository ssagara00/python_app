from django.test import TestCase
from django.urls import resolve, reverse

from crud_board.views import users


class TestsUrls(TestCase):
    """URLが正しいビュー関数にマッピングされているかテスト"""

    def test_list_url(self):
        url = reverse("crud_board:list")
        self.assertEqual(resolve(url).func, users.list)

    def test_new_url(self):
        url = reverse("crud_board:new")
        self.assertEqual(resolve(url).func, users.edit)

    def test_edit_url(self):
        url = reverse("crud_board:edit", args=[1])
        self.assertEqual(resolve(url).func, users.edit)

    def test_show_url(self):
        url = reverse("crud_board:show", args=[1])
        self.assertEqual(resolve(url).func, users.show)

    def test_delete_url(self):
        url = reverse("crud_board:delete", args=[1])
        self.assertEqual(resolve(url).func, users.delete)
