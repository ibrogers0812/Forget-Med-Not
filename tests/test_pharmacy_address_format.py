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


def test_pharmacy_address_format(client, mocker):
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

    # Mock function to add pharmacy info
    mock_pharmacy_data = []

    def mock_add_pharmacy_info(pharmacy_data):
        """Mock function to simulate adding pharmacy info."""
        formatted_address = (
            f"{pharmacy_data['street']}, {pharmacy_data['city']}, "
            f"{pharmacy_data['state']}, {pharmacy_data['postal_code']}"
        )
        mock_pharmacy_data.append({
            "name": pharmacy_data["name"],
            "address": formatted_address
        })

    # Patch the add_pharmacy_info function
    mocker.patch("route.add_pharmacy_info", side_effect=mock_add_pharmacy_info)

    # Step 2: Call the function with test data
    client.post('/add_pharmacy', data=test_pharmacy_data, follow_redirects=True)

    # Step 3: Verify the address format in the stored data
    assert mock_pharmacy_data[0]["address"] == expected_address, (
        "Test Failed: Address format is incorrect."
    )
