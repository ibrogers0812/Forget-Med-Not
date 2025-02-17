# Remove the unused import statement
# from datetime import datetime


def add_event(calendar, event):
    """
    Adds an event to the calendar.

    Parameters:
    - calendar: list of events
    - event: dictionary containing event details (e.g., title, date)
    """
    calendar.append(event)


def remove_event(calendar, event):
    """
    Removes an event from the calendar.
    
    Parameters:
    - calendar: list of events
    - event: dictionary containing event details (e.g., title, date)
    """
    if event in calendar:
        calendar.remove(event)


def list_events(calendar):
    """
    Lists all events in the calendar.
    
    Parameters:
    - calendar: list of events

    Returns:
    - List of events sorted by date
    """
    return sorted(calendar, key=lambda x: x['date'])


def get_events_for_date(calendar, date):
    """
    Gets all events for a specific date.

    Parameters:
    - calendar: list of events
    - date: target date to filter events

    Returns:
    - List of events on the specified date
    """
    return [event for event in calendar if event['date'] == date]
