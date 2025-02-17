import unittest
from calendar_functions import add_event, remove_event, list_events


class TestCalendarFunctions(unittest.TestCase):

    def setUp(self):
        self.calendar = []


    def test_add_event(self):
        event = {"title": "Doctor Appointment", "date": "2025-02-16"}
        add_event(self.calendar, event)
        self.assertIn(event, self.calendar)


    def test_remove_event(self):
        event = {"title": "Doctor Appointment", "date": "2025-02-16"}
        self.calendar.append(event)
        remove_event(self.calendar, event)
        self.assertNotIn(event, self.calendar)


    def test_list_events(self):
        event1 = {"title": "Doctor Appointment", "date": "2025-02-16"}
        event2 = {"title": "Pharmacy Visit", "date": "2025-02-17"}
        self.calendar.extend([event1, event2])
        events = list_events(self.calendar)
        self.assertEqual(events, [event1, event2])


if __name__ == '__main__':
    unittest.main()
