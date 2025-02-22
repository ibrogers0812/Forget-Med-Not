from flask import (
    Blueprint, request, jsonify
)
from datetime import datetime
from med_reminders import (
    add_reminder, delete_reminder, list_reminders  # Removed unused import `update_reminder`
)

main = Blueprint('main', __name__)
reminders = []  # Initialize the reminders list


@main.route('/add_reminder', methods=['POST'])
def add_reminder_view():  # Renamed to avoid conflict with the imported function
    data = request.form
    medication = data.get('medication')
    dose = data.get('dose')
    time = data.get('time')
    time = datetime.strptime(time, '%Y-%m-%d %H:%M:%S')

    reminder = {"medication": medication, "dose": dose, "time": time}
    add_reminder(reminders, medication, dose, time)

    return jsonify(reminder), 200


@main.route('/delete_reminder', methods=['POST'])
def delete_reminder_view():  # Renamed to avoid conflict with the imported function
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
def list_reminders_view():  # Renamed to avoid conflict with the imported function
    return jsonify(reminders), 200
