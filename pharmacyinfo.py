import json


def load_pharmacy_data(file_path):
    """
    Loads pharmacy data from a JSON file.

    Parameters:
    - file_path: path to the JSON file

    Returns:
    - List of pharmacies
    """
    with open(file_path, 'r') as file:
        pharmacies = json.load(file)
    return pharmacies


def get_pharmacy_info(pharmacies, name):
    """
    Retrieves information for a specific pharmacy by name.

    Parameters:
    - pharmacies: list of pharmacies
    - name: name of the pharmacy to retrieve information for

    Returns:
    - Dictionary containing pharmacy information or None if not found
    """
    for pharmacy in pharmacies:
        if pharmacy['name'].lower() == name.lower():
            return pharmacy
    return None


def add_pharmacy_info(pharmacies, new_pharmacy):
    """
    Adds new pharmacy information to the list.

    Parameters:
    - pharmacies: list of pharmacies
    - new_pharmacy: dictionary containing new pharmacy information

    Returns:
    - Updated list of pharmacies
    """
    pharmacies.append(new_pharmacy)
    return pharmacies


def update_pharmacy_info(pharmacies, name, updated_info):
    """
    Updates information for a specific pharmacy by name.

    Parameters:
    - pharmacies: list of pharmacies
    - name: name of the pharmacy to update
    - updated_info: dictionary containing updated pharmacy information

    Returns:
    - Updated list of pharmacies
    """
    for pharmacy in pharmacies:
        if pharmacy['name'].lower() == name.lower():
            pharmacy.update(updated_info)
            break
    return pharmacies


def delete_pharmacy_info(pharmacies, name):
    """
    Deletes a specific pharmacy by name.

    Parameters:
    - pharmacies: list of pharmacies
    - name: name of the pharmacy to delete

    Returns:
    - None (modifies the list in place)
    """
    pharmacies[:] = [
        pharmacy for pharmacy in pharmacies
        if pharmacy['name'].lower() != name.lower()
    ]
