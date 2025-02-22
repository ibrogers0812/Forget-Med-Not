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


def test_pharmacy_address_format(client):
    """
    Test case to check if the add_pharmacy_info function correctly
    formats the pharmacy's address.
    """

    # Step 1: Define test pharmacy information
    test_pharmacy_data = {
        "name": "Test Pharmacy",
        "street": "123 Main St",
        "city": "Orlando",
        "state": "FL",
        "postal_code": "32801"
    }

    # Expected formatted address
    expected_address = "123 Main St, Orlando, FL, 32801"

    # Step 2: Call the function with test data
    response = client.post(
        '/add_pharmacy',
        data=test_pharmacy_data,
        follow_redirects=True
    )

    assert response.status_code == 200  # Ensure request was successful

    # Step 3: Retrieve pharmacies and verify the address format
    pharmacies_response = client.get('/pharmacies')
    assert pharmacies_response.status_code == 200  # Ensure pharmacies are accessible

    # Parse response data
    response_data = pharmacies_response.get_json()
    added_pharmacy = next((p for p in response_data if p["name"] == "Test Pharmacy"), None)

    assert added_pharmacy is not None, "Test Failed: Pharmacy was not added"
    assert added_pharmacy["address"] == expected_address, "Test Failed: Address format is incorrect."
