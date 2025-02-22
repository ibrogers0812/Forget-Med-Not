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
    name = request.json.get("pharmacy_name")
    if not name:
        return "Missing pharmacy name", 400

    global pharmacies
    pharmacies[:] = [p for p in pharmacies if p['name'].lower() != name.lower()]

    return jsonify({"message": "Pharmacy removed successfully!"}), 200
