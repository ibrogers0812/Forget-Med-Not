import pytest
import json
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

    # Mock reading from file
    mock_read = mocker.patch(
        "builtins.open",
        mocker.mock_open(read_data=json.dumps(mock_pharmacy_data))
    )

    # Mock writing to file
    mock_write = mocker.patch("builtins.open", mocker.mock_open())

    # Step 2: Send a request to delete "Test Pharmacy"
    delete_data = {"pharmacy_name": "Test Pharmacy"}
    response = client.post(
        '/remove_pharmacy',
        data=json.dumps(delete_data),
        content_type='application/json',
        follow_redirects=True
    )

    assert response.status_code == 200  # Ensure request was successful

    # Ensure that the mock write operation was called at least once
    mock_write.assert_called_once_with("data/pharmacy_info.json", "w")
