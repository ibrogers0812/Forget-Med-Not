from datetime import datetime, timedelta
from googleapiclient.discovery import build
from calendar_auth import get_calendar_service

def add_medication_event(user_email, medication_name, dosage, reminder_time):
    """Adds a medication reminder to the user's Google Calendar"""
    service = build("calendar", "v3", credentials=get_calendar_service())

    event = {
        "summary": f"Take {medication_name} ({dosage})",
        "description": f"Reminder to take {medication_name} ({dosage}) on time.",
        "start": {
            "dateTime": reminder_time.isoformat(),
            "timeZone": "America/New_York"
        },
        "end": {
            "dateTime": (reminder_time + timedelta(minutes=10)).isoformat(),
            "timeZone": "America/New_York"
        },
        "reminders": {
            "useDefault": False,
            "overrides": [
                {"method": "popup", "minutes": 10},
                {"method": "email", "minutes": 30}
            ],
        },
    }
    #pylint: disable=E1101
    event = service.events().insert(calendarId="primary", body=event).execute()
    print(f"Medication reminder added: {event.get('htmlLink')}")
    return event.get("id")

def delete_medication_event(event_id):
    """Deletes a medication reminder from the user's Google Calendar"""
    service = build("calendar", "v3", credentials=get_calendar_service())
    #pylint: disable=E1101
    service.events().delete(calendarId="primary", eventId=event_id).execute()
    print(f"Deleted event {event_id}")
