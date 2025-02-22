import json
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

def test_remove_pharmacy(client, mocker):
    """
    Test case to check if a user can successfully remove a
    pharmacy's information.
    """

    # Step 1: Mock pharmacy data with an existing pharmacy
    mock_pharmacy_data = [
        {"name": "Test Pharmacy"},
        {"name": "Pharmacy B"},
        {"name": "Pharmacy C"}
    ]

    # Mock the file reading process
    mocker.patch(
        "builtins.open",
        mocker.mock_open(read_data=json.dumps(mock_pharmacy_data))
    )

    # Step 2: Send a request to delete "Test Pharmacy"
    delete_data = {"pharmacy_name": "Test Pharmacy"}
    response = client.post(
        '/remove_pharmacy',
        data=delete_data,
        follow_redirects=True
    )

    assert response.status_code == 200  # Ensure delete request was processed

    # Step 3: Retrieve pharmacy list and confirm removal
    response = client.get('/pharmacies')
    assert response.status_code == 200  # Ensure pharmacy list is accessible

    pharmacy_list = json.loads(response.data)
    search_result = next(
        (ph for ph in pharmacy_list if ph["name"] == "Test Pharmacy"),
        None
    )

    assert search_result is None, (
        "Test Failed: Pharmacy information was not removed."
    )
