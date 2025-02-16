import unittest
from unittest.mock import patch
from datetime import datetime, timedelta
from med_reminders import schedule_reminder, check_reminders, send_notification

class TestMedReminders(unittest.TestCase):

    def test_schedule_reminder(self):
        reminder = schedule_reminder("Aspirin", "1 tablet", 8)
        expected_next_dose_time = datetime.now() + timedelta(hours=8)
        
        self.assertEqual(reminder["medication_name"], "Aspirin")
        self.assertEqual(reminder["dose"], "1 tablet")
        # Allow a small delta for time difference
        self.assertAlmostEqual(reminder["next_dose_time"], expected_next_dose_time, delta=timedelta(seconds=1))

    @patch('builtins.print')
    def test_send_notification(self, mock_print):
        send_notification("Aspirin", "1 tablet")
        mock_print.assert_called_once_with("Reminder: It's time to take 1 tablet of Aspirin.")
    
    @patch('med_reminders.send_notification')
    def test_check_reminders(self, mock_send_notification):
        reminder = schedule_reminder("Aspirin", "1 tablet", -1)  # Use negative value to trigger reminder immediately
        reminders = [reminder]
        
        updated_reminders = check_reminders(reminders)
        
        mock_send_notification.assert_called_once_with("Aspirin", "1 tablet")
        # Check if the next dose time is updated correctly
        expected_next_dose_time = datetime.now() + timedelta(hours=8)
        self.assertAlmostEqual(updated_reminders[0]["next_dose_time"], expected_next_dose_time, delta=timedelta(seconds=1))

if __name__ == '__main__':
    unittest.main()
