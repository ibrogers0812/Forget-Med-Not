import pytest
from flask import Flask
from datetime import datetime
from route import main  # Import the Flask blueprint

@pytest.fixture
def client():
    """Set up a test client for the Flask application."""
    app = Flask(__name__)
    app.register_blueprint(main)
    app.config['TESTING'] = True
    return app.test_client()

def test_add_more_than_five_medications(client):
    """
    Test case to check if a user can add more than five active medications.
    """

    # Step 1: Add five medication reminders
    for i in range(1, 6):
        reminder_data = {
            "medication": f"Medication {i}",
            "dose": "100mg",
            "time": f"2025-02-18 08:0{i}:00"
        }
        response = client.post('/add_reminder', data=reminder_data, follow_redirects=True)
        assert response.status_code == 200  # Ensure each reminder is added successfully

    # Step 2: Attempt to add a sixth medication
    extra_reminder_data = {
        "medication": "Medication 6",
        "dose": "50mg",
        "time": "2025-02-18 09:00:00"
    }
    response = client.post('/add_reminder', data=extra_reminder_data, follow_redirects=True)

    # Step 3: Retrieve reminders and check if more than five exist
    reminders_response = client.get('/list_reminders')
    
    assert reminders_response.status_code == 200  # Ensure reminders list is accessible
    reminders_text = reminders_response.get_data(as_text=True)

    # Count occurrences of 'Medication' in the response
    medication_count = reminders_text.count("Medication")

    assert medication_count <= 5, "Test Failed: More than five medications were added."
