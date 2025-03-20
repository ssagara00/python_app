from django.test import Client, TestCase
from django.urls import reverse

from crud_board.forms import HouseEstimateForm
from crud_board.models import HouseEstimate


class TestsHouseEstimateView(TestCase):

    def setUp(self):
        self.client = Client()
        self.house_estimate = HouseEstimate.objects.create(
            estimate_company="Test Company",
            contact_person="Test Person",
            property_address="123 Test St",
            estimate=12345.67,
            layout_memo="Test layout memo",
            sunlight_memo="Test sunlight memo",
            memo="Test memo",
            created_by="Tester",
            updated_by="Tester",
        )

    def test_index_get(self):
        response = self.client.get(reverse("crud_board:house_estimate_index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "house_estimate/index.html")
        self.assertContains(response, "Test Company")

    def test_new_get(self):
        response = self.client.get(reverse("crud_board:house_estimate_new"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "house_estimate/new.html")
        self.assertIsInstance(response.context["form"], HouseEstimateForm)

    def test_new_post(self):
        data = {
            "estimate_company": "New Company",
            "contact_person": "New Person",
            "property_address": "456 New St",
            "estimate": 67890.12,
            "layout_memo": "New layout memo",
            "sunlight_memo": "New sunlight memo",
            "memo": "New memo",
            "created_by": "New Tester",
            "updated_by": "New Tester",
        }
        response = self.client.post(reverse("crud_board:house_estimate_new"), data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(
            HouseEstimate.objects.filter(estimate_company="New Company").exists()
        )
