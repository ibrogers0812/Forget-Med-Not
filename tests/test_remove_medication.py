import pytest
from flask import Flask
from route import main  # Import the Flask blueprint


@pytest.fixture
def client():
    """Set up a test client for the Flask application."""
    app = Flask(__name__)
    app.register_blueprint(main)
    app.config['TESTING'] = True
    app.config['SECRET_KEY'] = 'your_secret_key_here'  # Set the secret key
    return app.test_client()


def test_remove_medication_reminder(client):
    """
    Test case to check if a user can successfully remove a
    medication reminder.
    """

    # Step 1: Add a test medication reminder
    test_medication = "Ibuprofen"
    test_time = "2025-02-18 09:00:00"

    reminder_data = {
        "medication": test_medication,
        "dose": "200mg",
        "time": test_time
    }

    # Add the medication reminder
    client.post('/add_reminder', data=reminder_data, follow_redirects=True)

    # Step 2: Remove the added reminder
    delete_data = {"time": test_time}
    response = client.post('/delete_reminder', data=delete_data, follow_redirects=True)

    assert response.status_code == 200  # Ensure delete request was processed

    # Step 3: Retrieve reminders and confirm removal
    reminders_response = client.get('/list_reminders')
    assert reminders_response.status_code == 200  # Reminders are accessible

    assert test_medication not in reminders_response.get_data(as_text=True), \
        "Test Failed: Medication reminder was not removed."
