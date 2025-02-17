import unittest
from datetime import datetime, timedelta
from med_reminders import (
    add_reminder, update_reminder, delete_reminder, list_reminders
)


class TestMedReminders(unittest.TestCase):

    def setUp(self):
        self.reminders = []

    def test_add_reminder(self):
        reminder = {
            "medication": "Aspirin",
            "dose": "100mg",
            "time": datetime.now() + timedelta(hours=1)
        }
        add_reminder(self.reminders, reminder)
        self.assertIn(reminder, self.reminders)

    def test_update_reminder(self):
        reminder = {
            "medication": "Aspirin",
            "dose": "100mg",
            "time": datetime.now() + timedelta(hours=1)
        }
        self.reminders.append(reminder)
        new_time = datetime.now() + timedelta(hours=2)
        update_reminder(self.reminders, reminder, new_time)
        self.assertEqual(self.reminders[0]["time"], new_time)

    def test_delete_reminder(self):
        reminder = {
            "medication": "Aspirin",
            "dose": "100mg",
            "time": datetime.now() + timedelta(hours=1)
        }
        self.reminders.append(reminder)
        delete_reminder(self.reminders, reminder)
        self.assertNotIn(reminder, self.reminders)

    def test_list_reminders(self):
        reminder1 = {
            "medication": "Aspirin",
            "dose": "100mg",
            "time": datetime.now() + timedelta(hours=1)
        }
        reminder2 = {
            "medication": "Ibuprofen",
            "dose": "200mg",
            "time": datetime.now() + timedelta(hours=2)
        }
        self.reminders.extend([reminder1, reminder2])
        reminders = list_reminders(self.reminders)
        self.assertEqual(reminders, [reminder1, reminder2])


if __name__ == '__main__':
    unittest.main()
