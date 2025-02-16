pip install ics

from ics import Calendar, Event
from datetime import datetime, timedelta

# Function to create a new calendar event for medication reminders
def create_event(name, start_time, duration_minutes):
    event = Event()
    event.name = name
    event.begin = start_time
    event.duration = timedelta(minutes=duration_minutes)
    return event

# Function to add an event to a calendar
def add_event_to_calendar(calendar, event):
    calendar.events.add(event)

# Function to save the calendar to a file
def save_calendar_to_file(calendar, filename):
    with open(filename, 'w') as f:
        f.writelines(calendar)

# Example usage
if __name__ == "__main__":
    cal = Calendar()
    
    # Schedule a medication reminder
    med_name = "Aspirin"
    start_time = datetime(2025, 2, 16, 9, 0)  # 9:00 AM on Feb 16, 2025
    duration_minutes = 5
    
    event = create_event(f"Take {med_name}", start_time, duration_minutes)
    add_event_to_calendar(cal, event)
    
    # Save the calendar to a file
    save_calendar_to_file(cal, 'medication_reminders.ics')
    
    print("Medication reminder event created and saved to medication_reminders.ics")
