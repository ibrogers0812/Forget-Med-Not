from datetime import datetime, timedelta
import time

# Function to schedule medication reminders
def schedule_reminder(medication_name, dose, frequency_in_hours):
    next_dose_time = datetime.now() + timedelta(hours=frequency_in_hours)
    return {"medication_name": medication_name, "dose": dose, "next_dose_time": next_dose_time}

# Function to send a notification (placeholder)
def send_notification(medication_name, dose):
    print(f"Reminder: It's time to take {dose} of {medication_name}.")

# Function to check and send reminders
def check_reminders(reminders):
    current_time = datetime.now()
    for reminder in reminders:
        if reminder["next_dose_time"] <= current_time:
            send_notification(reminder["medication_name"], reminder["dose"])
            reminder["next_dose_time"] = current_time + timedelta(hours=8)  # Schedule next dose (adjust frequency as needed)
    return reminders

# Example usage
if __name__ == "__main__":
    reminders = []
    reminders.append(schedule_reminder("Aspirin", "1 tablet", 8))
    reminders.append(schedule_reminder("Vitamin D", "1 capsule", 24))
    
    # Main loop to continuously check for reminders
    while True:
        reminders = check_reminders(reminders)
        time.sleep(60)  # Check every minute
