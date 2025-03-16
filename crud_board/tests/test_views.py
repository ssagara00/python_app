from django.test import Client, TestCase
from django.urls import reverse

from crud_board.models import User


class TestsViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(
            name="Test User", email="test@example.com", age=20
        )

    def test_list_view(self):
        """GET メソッドでアクセスしてステータスコード200を返されることを確認"""
        response = self.client.get(reverse("crud_board:list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "crud_board/list.html")
        self.assertContains(response, "Test User")

    def test_edit_view_get(self):
        response = self.client.get(reverse("crud_board:edit", args=[self.user.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "crud_board/edit.html")
        self.assertContains(response, "Test User")

    def test_edit_view_post(self):
        response = self.client.post(
            reverse("crud_board:edit", args=[self.user.id]),
            {"name": "Updated User", "email": "updated@example.com"},
        )
        self.assertEqual(response.status_code, 302)
        self.user.refresh_from_db()
        self.assertEqual(self.user.name, "Updated User")
        self.assertEqual(self.user.email, "updated@example.com")

    def test_delete_view_post(self):
        response = self.client.post(reverse("crud_board:delete", args=[self.user.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(User.objects.filter(id=self.user.id).exists())

    def test_show_view(self):
        response = self.client.get(reverse("crud_board:show", args=[self.user.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "crud_board/show.html")
        self.assertContains(response, "Test User")

    def tearDown(self):
        self.user = User.objects.create(
            name="Test User", email="test@example.com", age=20
        )
