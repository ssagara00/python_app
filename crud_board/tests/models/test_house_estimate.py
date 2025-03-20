from django.test import TestCase
from crud_board.models.house_estimate import HouseEstimate


class HouseEstimateModelTest(TestCase):

    def setUp(self):
        self.house_estimate = HouseEstimate.objects.create(
            estimate_company="Test Company",
            contact_person="Test Person",
            property_address="123 Test St",
            estimate=12345.67,
            layout_memo="Test layout memo",
            sunlight_memo="Test sunlight memo",
            memo="Test memo",
            created_by="Tester",
            updated_by="Tester"
        )

    def test_house_estimate_creation(self):
        self.assertEqual(self.house_estimate.estimate_company, "Test Company")
        self.assertEqual(self.house_estimate.contact_person, "Test Person")
        self.assertEqual(self.house_estimate.property_address, "123 Test St")
        self.assertEqual(self.house_estimate.estimate, 12345.67)
        self.assertEqual(self.house_estimate.layout_memo, "Test layout memo")
        self.assertEqual(self.house_estimate.sunlight_memo, "Test sunlight memo")
        self.assertEqual(self.house_estimate.memo, "Test memo")
        self.assertEqual(self.house_estimate.created_by, "Tester")
        self.assertEqual(self.house_estimate.updated_by, "Tester")
