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

    client.post('/add_reminder', data=reminder_data, follow_redirects=True)

    update_data = {"old_time": old_time, "new_time": new_time}
    response = client.post('/update_reminder',
                           data=update_data, follow_redirects=True)

    assert response.status_code == 200, (
        "Test Failed: Update request did not return a successful response"
    )

    # Step 3: Retrieve reminders and verify the update
    reminders_response = client.get(
        '/list_reminders')
    # Reminders should be accessible
    assert reminders_response.status_code == 200

    reminders_json = reminders_response.get_json()
    updated_reminder = next(
        (r for r in reminders_json if r["medication"] == "Aspirin"),
        None
    )

    assert updated_reminder is not None, "Test Failed: Reminder was not found"
    assert (
        updated_reminder["time"] ==
        new_time
    ), (f"Test Failed: Reminder time was not updated, found "
        f"{updated_reminder['time']}")
