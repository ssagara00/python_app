from django.test import TestCase

from crud_board.models import User


class TestUser(TestCase):

    def setUp(self):
        self.user = User.objects.create(
            name="テストユーザー", email="test@example.com", age=30
        )

    def test_user_creation(self):
        self.assertEqual(self.user.name, "テストユーザー")
        self.assertEqual(self.user.email, "test@example.com")
        self.assertEqual(self.user.age, 30)

    def test_user_str(self):
        self.assertEqual(str(self.user), "テストユーザー")

    def tearDown(self):
        self.user = User.objects.create(
            name="Test User", email="test@example.com", age=20
        )
