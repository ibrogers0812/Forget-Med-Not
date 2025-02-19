import json
import pytest
from route import main  # Import the Flask blueprint
from flask import Flask


@pytest.fixture
def client():
    """Set up a test client for the Flask application."""
    app = Flask(__name__)
    app.register_blueprint(main)
    app.config['TESTING'] = True
    return app.test_client()


def test_search_unknown_pharmacy(client, mocker):
    """
    Test case to check if searching for a non-existent pharmacy returns "none"
    or an appropriate 'not found' message.
    """

    # Mock pharmacy data (ensure the searched pharmacy is NOT in this list)
    mock_pharmacy_data = [
        {"name": "Pharmacy A"},
        {"name": "Pharmacy B"},
        {"name": "Pharmacy C"}
    ]

    # Mock the file reading process to return predefined data
    mocker.patch("builtins.open", mocker.mock_open(read_data=json.dumps(mock_pharmacy_data)))

    # Perform a search for a non-existent pharmacy
    response = client.get('/pharmacies')
    
    assert response.status_code == 200  # Ensure the route is accessible

    # Check if the unknown pharmacy is NOT in the returned pharmacy list
    pharmacy_list = json.loads(response.data)
    search_result = next((ph for ph in pharmacy_list if ph['name'] == "Unknown Pharmacy"), None)

    assert search_result is None, "Test Failed: Unexpected pharmacy found"
