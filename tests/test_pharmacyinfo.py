import unittest
from io import StringIO
from unittest.mock import patch
import json
import os
from pharmacyinfo import getPharmacyInfo, loadPharmacyInfo

class TestPharmacyInfo(unittest.TestCase):

    @patch('builtins.input', side_effect=["Y", "My Pharmacy", "123-456-7890", "123 Main Street, Cityville, State, 12345"])
    @patch('builtins.print')
    def test_getPharmacyInfo(self, mock_print, mock_input):
        with patch('builtins.open', new_callable=unittest.mock.mock_open()) as mock_file:
            getPharmacyInfo()
            # Check if the file has been written to
            mock_file.assert_called_once_with('pharmacy_info.json', 'w')
            # Check the content written to the file
            written_content = json.loads(mock_file().write.call_args[0][0])
            expected_content = {
                "name": "My Pharmacy",
                "phone_number": "123-456-7890",
                "address": "123 Main Street, Cityville, State, 12345"
            }
            self.assertEqual(written_content, expected_content)

    @patch('builtins.print')
    def test_loadPharmacyInfo(self, mock_print):
        # Create a mock pharmacy_info.json file
        pharmacy_info = {
            "name": "My Pharmacy",
            "phone_number": "123-456-7890",
            "address": "123 Main Street, Cityville, State, 12345"
        }
        with open('pharmacy_info.json', 'w') as f:
            json.dump(pharmacy_info, f)

        loadPharmacyInfo()

        # Check that the correct output was printed
        mock_print.assert_any_call("Pharmacy Name:", "My Pharmacy")
        mock_print.assert_any_call("Pharmacy Phone Number:", "123-456-7890")
        mock_print.assert_any_call("Pharmacy Address:", "123 Main Street, Cityville, State, 12345")

        # Clean up the mock file
        os.remove('pharmacy_info.json')

if __name__ == '__main__':
    unittest.main()
