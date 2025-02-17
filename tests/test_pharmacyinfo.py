import unittest
from pharmacyinfo import (
    get_pharmacy_info, add_pharmacy_info, 
    update_pharmacy_info, delete_pharmacy_info
)


class TestPharmacyInfo(unittest.TestCase):

    def setUp(self):
        self.pharmacies = [
            {
                "name": "HealthFirst Pharmacy",
                "address": "1234 Health St, Lake Worth, FL 33460",
                "phone": "+1-555-123-4567",
                "email": "contact@healthfirstpharmacy.com",
                "hours": {
                    "Monday": "9AM - 9PM",
                    "Tuesday": "9AM - 9PM",
                    "Wednesday": "9AM - 9PM",
                    "Thursday": "9AM - 9PM",
                    "Friday": "9AM - 9PM",
                    "Saturday": "9AM - 7PM",
                    "Sunday": "11AM - 6PM"
                }
            }
        ]

    def test_get_pharmacy_info(self):
        pharmacy_name = "HealthFirst Pharmacy"
        info = get_pharmacy_info(self.pharmacies, pharmacy_name)
        self.assertIsNotNone(info)
        self.assertEqual(info["name"], pharmacy_name)

    def test_add_pharmacy_info(self):
        new_pharmacy = {
            "name": "Wellness Pharmacy",
            "address": "5678 Wellness Ave, Lake Worth, FL 33460",
            "phone": "+1-555-987-6543",
            "email": "info@wellnesspharmacy.com",
            "hours": {
                "Monday": "9AM - 9PM",
                "Tuesday": "9AM - 9PM",
                "Wednesday": "9AM - 9PM",
                "Thursday": "9AM - 9PM",
                "Friday": "9AM - 9PM",
                "Saturday": "9AM - 7PM",
                "Sunday": "11AM - 6PM"
            }
        }
        add_pharmacy_info(self.pharmacies, new_pharmacy)
        self.assertIn(new_pharmacy, self.pharmacies)

    def test_update_pharmacy_info(self):
        pharmacy_name = "HealthFirst Pharmacy"
        new_info = {
            "phone": "+1-555-000-0000"
        }
        update_pharmacy_info(self.pharmacies, pharmacy_name, new_info)
        updated_info = get_pharmacy_info(self.pharmacies, pharmacy_name)
        self.assertEqual(updated_info["phone"], "+1-555-000-0000")

    def test_delete_pharmacy_info(self):
        pharmacy_name = "HealthFirst Pharmacy"
        delete_pharmacy_info(self.pharmacies, pharmacy_name)
        info = get_pharmacy_info(self.pharmacies, pharmacy_name)
        self.assertIsNone(info)


if __name__ == '__main__':
    unittest.main()
