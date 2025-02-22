# Removed unused import

def add_reminder(reminders, medication, dose, time):
    """
    Adds a reminder to the list.

    Parameters:
    - reminders: list of reminders
    - medication: name of the medication
    - dose: dose of the medication
    - time: time of the reminder
    """
    reminder = {
        "medication": medication,
        "dose": dose,
        "time": time
    }
    reminders.append({"medication": medication, "dose": dose, "time": time})


def update_reminder(reminders, old_reminder, new_time):
    """
    Updates the time of an existing reminder.

    Parameters:
    - reminders: list of reminders
    - old_reminder: the reminder to be updated
    - new_time: new time for the reminder
    """
    for reminder in reminders:
        if reminder == old_reminder:
            reminder["time"] = new_time
            break


def delete_reminder(reminders, reminder_to_delete):
    """
    Deletes a reminder from the list.

    Parameters:
    - reminders: list of reminders
    - reminder_to_delete: the reminder to be deleted
    """
    if reminder_to_delete in reminders:
        reminders.remove(reminder_to_delete)


def list_reminders(reminders):
    """
    Lists all reminders sorted by time.

    Parameters:
    - reminders: list of reminders

    Returns:
    - List of reminders sorted by time
    """
    return sorted(reminders, key=lambda x: x["time"])


def get_reminders_for_time(reminders, time):
    """
    Gets all reminders for a specific time.

    Parameters:
    - reminders: list of reminders
    - time: target time to filter reminders

    Returns:
    - List of reminders at the specified time
    """
    return [reminder for reminder in reminders if reminder["time"] == time]
