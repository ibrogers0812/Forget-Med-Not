import json
import unittest

class TestPharmacyInfo(unittest.TestCase):
    def setUp(self):
        self.pharmacy_data = [
            {
                "name": "Publix Pharmacy",
                "address": "1234 Health St, Lake Worth, FL 33467",
                "phone": "+1-888-123-4567",
                "email": "contact@publixpharmacy.com",
                "hours": {
                    "Monday": "9AM - 9PM",
                    "Tuesday": "9AM - 9PM",
                    "Wednesday": "9AM - 9PM",
                    "Thursday": "9AM - 9PM",
                    "Friday": "9AM - 9PM",
                    "Saturday": "9AM - 7PM",
                    "Sunday": "11AM - 6PM"
                }
            },
            {
                "name": "Wellness Pharmacy",
                "address": "5678 Wellness Ave, Lake Worth, FL 33467",
                "phone": "+1-888-987-6543",
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
        ]

    def test_pharmacy_names(self):
        self.assertEqual(self.pharmacy_data[0]['name'], "Publix Pharmacy")
        self.assertEqual(self.pharmacy_data[1]['name'], "Wellness Pharmacy")

    def test_pharmacy_addresses(self):
        self.assertEqual(self.pharmacy_data[0]['address'], "1234 Health St, Lake Worth, FL 33467")
        self.assertEqual(self.pharmacy_data[1]['address'], "5678 Wellness Ave, Lake Worth, FL 33467")

    def test_pharmacy_phones(self):
        self.assertEqual(self.pharmacy_data[0]['phone'], "+1-888-123-4567")
        self.assertEqual(self.pharmacy_data[1]['phone'], "+1-888-987-6543")

    def test_pharmacy_emails(self):
        self.assertEqual(self.pharmacy_data[0]['email'], "contact@publixpharmacy.com")
        self.assertEqual(self.pharmacy_data[1]['email'], "info@wellnesspharmacy.com")

    def test_pharmacy_hours(self):
        expected_hours_publix = {
            "Monday": "9AM - 9PM",
            "Tuesday": "9AM - 9PM",
            "Wednesday": "9AM - 9PM",
            "Thursday": "9AM - 9PM",
            "Friday": "9AM - 9PM",
            "Saturday": "9AM - 7PM",
            "Sunday": "11AM - 6PM"
        }
        expected_hours_wellness = {
            "Monday": "9AM - 9PM",
            "Tuesday": "9AM - 9PM",
            "Wednesday": "9AM - 9PM",
            "Thursday": "9AM - 9PM",
            "Friday": "9AM - 9PM",
            "Saturday": "9AM - 7PM",
            "Sunday": "11AM - 6PM"
        }
        self.assertEqual(self.pharmacy_data[0]['hours'], expected_hours_publix)
        self.assertEqual(self.pharmacy_data[1]['hours'], expected_hours_wellness)

if __name__ == '__main__':
    unittest.main()
