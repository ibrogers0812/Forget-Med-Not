import json
from flask import (
    Blueprint, request, jsonify
)
from datetime import datetime
from med_reminders import (
    add_reminder, delete_reminder  # Removed unused import `list_reminders`
)

main = Blueprint('main', __name__)
reminders = []  # Initialize the reminders list
pharmacies = []  # Define the pharmacies list


@main.route('/add_reminder', methods=['POST'])
def add_reminder_view():
    data = request.form
    medication = data.get('medication')
    dose = data.get('dose')
    time = data.get('time')
    time = datetime.strptime(time, '%Y-%m-%d %H:%M:%S')

    reminder = {"medication": medication, "dose": dose, "time": time}
    add_reminder(reminders, medication, dose, time)

    return jsonify(reminder), 200


@main.route('/delete_reminder', methods=['POST'])
def delete_reminder_view():
    data = request.form
    time = data.get('time')
    time = datetime.strptime(time, '%Y-%m-%d %H:%M:%S')

    reminder_to_delete = next(
        (r for r in reminders if r['time'] == time), None
    )

    if reminder_to_delete:
        delete_reminder(reminders, reminder_to_delete)

    return jsonify({"message": "Reminder deleted successfully!"}), 200


@main.route('/list_reminders', methods=['GET'])
def list_reminders_view():
    return jsonify(reminders), 200


@main.route('/remove_pharmacy', methods=['POST'])
def remove_pharmacy():
    """
    Endpoint to remove a pharmacy from the list.
    """
    data = request.json
    name = data.get("pharmacy_name")

    if not name:
        return jsonify({"error": "Missing pharmacy name"}), 400

    global pharmacies
    pharmacies = [p for p in pharmacies if p['name'].lower() != name.lower()]

    try:
        with open("data/pharmacy_info.json", "w") as file:
            json.dump(pharmacies, file)
    except Exception as e:
        return jsonify({"error": f"Failed to update file: {str(e)}"}), 500

    return jsonify({"message": "Pharmacy removed successfully!"}), 200


@main.route('/add_pharmacy', methods=['POST'])
def add_pharmacy():
    data = request.form
    name = data.get("name")
    street = data.get("street")
    city = data.get("city")
    state = data.get("state")
    postal_code = data.get("postal_code")

    if not all([name, street, city, state, postal_code]):
        return jsonify({"error": "Missing required fields"}), 400

    formatted_address = f"{street}, {city}, {state}, {postal_code}"
    pharmacy_entry = {"name": name, "address": formatted_address}

    pharmacies.append(pharmacy_entry)  # Add to list

    return jsonify(pharmacy_entry), 200  # Ensure JSON response


@main.route('/pharmacies', methods=['GET'])
def pharmacies_view():
    return jsonify(pharmacies), 200


@main.route('/update_reminder', methods=['POST'])
def update_reminder_view():
    data = request.form
    old_time = data.get('old_time')
    new_time = data.get('new_time')

    if not old_time or not new_time:
        return jsonify({"error": "Missing required fields"}), 400

    old_time = datetime.strptime(old_time, '%Y-%m-%d %H:%M:%S')
    new_time = datetime.strptime(new_time, '%Y-%m-%d %H:%M:%S')

    old_reminder = next((r for r in reminders if r['time'] == old_time), None)
    if old_reminder:
        old_reminder["time"] = new_time
        return jsonify({"message": "Reminder updated successfully!"}), 200

    return jsonify({"error": "Reminder not found"}), 404
