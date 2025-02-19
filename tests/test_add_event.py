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


def test_add_event_to_calendar(client):
    """
    Test case to check if a user can successfully add an event to the calendar.
    """

    # Step 1: Define event details
    event_data = {
        "title": "Doctor Appointment",
        "date": "2025-02-20",
        "time": "14:30:00",
        "description": "Annual health check-up"
    }

    # Step 2: Send a request to add the event
    response = client.post('/add_event', data=event_data, follow_redirects=True)

    assert response.status_code == 200  # Ensure the request was successful

    # Step 3: Retrieve events and check if the new event exists
    events_response = client.get('/list_events')

    assert events_response.status_code == 200  # Ensure event list is accessible
    assert "Doctor Appointment" in events_response.get_data(as_text=True), "Test Failed: Event was not added successfully."
