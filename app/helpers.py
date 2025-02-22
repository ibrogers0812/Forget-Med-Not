# helpers.py

import datetime

def format_date(date_str):
    """
    Convert a date string in 'YYYY-MM-DD' format to a datetime object.

    Args:
        date_str (str): The date string in 'YYYY-MM-DD' format.

    Returns:
        datetime.date: The corresponding datetime object.
    """
    return datetime.datetime.strptime(date_str, "%Y-%m-%d").date()


def days_until(date):
    """
    Calculate the number of days from today until the specified date.

    Args:
        date (datetime.date): The target date.

    Returns:
        int: Number of days until the specified date.
    """
    today = datetime.date.today()
    delta = date - today
    return delta.days


def validate_event_data(event_data):
    """
    Validate the event data dictionary to ensure required fields are present.

    Args:
        event_data (dict): Dictionary containing event details.

    Returns:
        bool: True if all required fields are present, False otherwise.
    """
    required_fields = {'title', 'date', 'time', 'description'}
    return required_fields <= event_data.keys()


def format_event_for_display(event_data):
    """
    Format event data for display.
    
    Args:
        event_data (dict): Dictionary containing event details.

    Returns:
        str: Formatted string for event display.
    """
    return f"Event: {event_data['title']} on {event_data['date']} at {event_data['time']} - {event_data['description']}"


def send_notification(message):
    """
    Send a notification to the user.

    Args:
        message (str): The notification message to send.

    This is a placeholder function. The actual implementation will depend
    on the notification method used (e.g., email, SMS, push notification).
    """
    print(f"Notification: {message}")
