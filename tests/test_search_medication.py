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


def test_search_medication(client):
    """
    Test case to check if a user can search for a medication by name.
    """

    # Step 1: Add a test medication reminder
    test_medication = "Aspirin"
    reminder_data = {
        "medication": test_medication,
        "dose": "100mg",
        "time": "2025-02-18 08:00:00"
    }

    # Add the medication to the system
    client.post(
        '/add_reminder',
        data=reminder_data,
        follow_redirects=True
    )

    # Step 2: Perform a search request
    response = client.get(f'/list_reminders?search={test_medication}')

    assert response.status_code == 200  # Ensure the request was successful

    # Step 3: Verify if the medication appears in the response
    assert (
        test_medication in response.get_data(as_text=True)
    ), "Test Failed: Medication not found in search results."