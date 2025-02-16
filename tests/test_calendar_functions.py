import unittest
from datetime import datetime, timedelta
from ics import Calendar, Event
from calendar_functions import create_event, add_event_to_calendar, save_calendar_to_file
import os

class TestCalendarFunctions(unittest.TestCase):

    def test_create_event(self):
        event_name = "Take Aspirin"
        start_time = datetime(2025, 2, 16, 9, 0)  # 9:00 AM on Feb 16, 2025
        duration_minutes = 5

        event = create_event(event_name, start_time, duration_minutes)

        self.assertEqual(event.name, event_name)
        self.assertEqual(event.begin.datetime, start_time)
        self.assertEqual(event.duration, timedelta(minutes=duration_minutes))

    def test_add_event_to_calendar(self):
        cal = Calendar()
        event_name = "Take Aspirin"
        start_time = datetime(2025, 2, 16, 9, 0)  # 9:00 AM on Feb 16, 2025
        duration_minutes = 5

        event = create_event(event_name, start_time, duration_minutes)
        add_event_to_calendar(cal, event)

        self.assertIn(event, cal.events)

    def test_save_calendar_to_file(self):
        cal = Calendar()
        event_name = "Take Aspirin"
        start_time = datetime(2025, 2, 16, 9, 0)  # 9:00 AM on Feb 16, 2025
        duration_minutes = 5

        event = create_event(event_name, start_time, duration_minutes)
        add_event_to_calendar(cal, event)

        filename = 'test_calendar.ics'
        save_calendar_to_file(cal, filename)

        self.assertTrue(os.path.exists(filename))

        # Clean up the test file
        os.remove(filename)

if __name__ == '__main__':
    unittest.main()
