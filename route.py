from flask import Blueprint, render_template, request, redirect, url_for, flash
from datetime import datetime
from med_reminders import add_reminder, update_reminder, delete_reminder, list_reminders
import json


main = Blueprint('main', __name__)
reminders = []  # Initialize the reminders list


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/add_reminder', methods=['GET', 'POST'])
def add_reminder_view():
    if request.method == 'POST':
        medication = request.form.get('medication')
        dose = request.form.get('dose')
        time = request.form.get('time')
        time = datetime.strptime(time, '%Y-%m-%d %H:%M:%S')
        reminder = {"medication": medication, "dose": dose, "time": time}
        add_reminder(reminders, reminder)
        flash('Reminder added successfully!')
        return redirect(url_for('main.index'))
    return render_template('add_reminder.html')


@main.route('/update_reminder', methods=['GET', 'POST'])
def update_reminder_view():
    if request.method == 'POST':
        old_time = request.form.get('old_time')
        new_time = request.form.get('new_time')
        old_time = datetime.strptime(old_time, '%Y-%m-%d %H:%M:%S')
        new_time = datetime.strptime(new_time, '%Y-%m-%d %H:%M:%S')
        old_reminder = next((r for r in reminders if r['time'] == old_time), None)
        if old_reminder:
            update_reminder(reminders, old_reminder, new_time)
            flash('Reminder updated successfully!')
        return redirect(url_for('main.index'))
    return render_template('update_reminder.html')


@main.route('/delete_reminder', methods=['POST'])
def delete_reminder_view():
    time = request.form.get('time')
    time = datetime.strptime(time, '%Y-%m-%d %H:%M:%S')
    reminder_to_delete = next((r for r in reminders if r['time'] == time), None)
    if reminder_to_delete:
        delete_reminder(reminders, reminder_to_delete)
        flash('Reminder deleted successfully!')
    return redirect(url_for('main.index'))


@main.route('/list_reminders')
def list_reminders_view():
    reminder_list = list_reminders(reminders)
    return render_template('list_reminders.html', reminders=reminder_list)


@main.route('/pharmacies')
def pharmacies_view():
    with open('data/pharmacy_info.json', 'r') as file:
        pharmacies = json.load(file)
    return render_template('pharmacies.html', pharmacies=pharmacies)
