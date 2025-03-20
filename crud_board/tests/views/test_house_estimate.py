from django.test import Client, TestCase
from django.urls import reverse

from crud_board.forms import HouseEstimateForm
from crud_board.models import HouseEstimate


class TestsHouseEstimateView(TestCase):

    def setUp(self):
        self.client = Client()

    def test_new_get(self):
        response = self.client.get(reverse("crud_board:house_estimate_new"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "house_estimate/new.html")
        self.assertIsInstance(response.context["form"], HouseEstimateForm)
