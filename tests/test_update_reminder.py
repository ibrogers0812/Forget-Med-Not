import pytest
from flask import Flask
from route import main  # Import the Flask blueprint

@pytest.fixture
def client():
    """Set up a test client for the Flask application."""
    app = Flask(__name__)
    app.register_blueprint(main)
    app.config['TESTING'] = True
    return app.test_client()

def test_update_medication_reminder_time(client):
    """
    Test case to check if a user can successfully update the time of an
    existing medication reminder.
    """

    # Step 1: Add a test reminder
    old_time = "2025-02-18 08:00:00"
    new_time = "2025-02-18 10:30:00"

    reminder_data = {
        "medication": "Aspirin",
        "dose": "100mg",
        "time": old_time
    }

    # Add a reminder first
    client.post(
        '/add_reminder',
        data=reminder_data,
        follow_redirects=True
    )

    # Step 2: Update the time of the existing reminder
    update_data = {
        "old_time": old_time,
        "new_time": new_time
    }

    response = client.post(
        '/update_reminder',
        data=update_data,
        follow_redirects=True
    )

    assert response.status_code == 200  # Update was processed successfully

    # Step 3: Retrieve reminders and verify the update
    reminders_response = client.get('/list_reminders')

    assert reminders_response.status_code == 200  # Reminders are accessible
    assert (
        new_time in reminders_response.get_data(as_text=True)
    ), "Test Failed: Reminder time was not updated"
