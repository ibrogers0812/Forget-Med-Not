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


def test_add_multiple_medications(client):
    """
    Test case to check if a user can add any number of active medications.
    """

    # Step 1: Add multiple medication reminders
    for i in range(1, 11):  # Example: Adding ten medication reminders
        reminder_data = {
            "medication": f"Medication {i}",
            "dose": "100mg",
            "time": f"2025-02-18 08:0{i}:00"
        }
        response = client.post(
            '/add_reminder',
            data=reminder_data,
            follow_redirects=True
        )
        assert response.status_code == 200  # Successfully add reminders

    # Step 2: Retrieve reminders and check if all were added
    reminders_response = client.get('/list_reminders')

    assert reminders_response.status_code == 200  # List is accessible
    reminders_text = reminders_response.get_data(as_text=True)

    # Count occurrences of 'Medication' in the response
    medication_count = reminders_text.count(
        "Medication"
    )

    # Example: Check if at least ten medications were added
    assert medication_count >= 10, (
        "Test Failed: Not all medications were added successfully."
    )
