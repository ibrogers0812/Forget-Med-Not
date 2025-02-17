from datetime import datetime
from flask import Flask
app = Flask(__name__)
from flask import request, redirect, url_for, flash
from flask_login import login_required, current_user
from models import db, Medication
from calendar_integration import add_medication_event, delete_medication_event

@app.route("/add_medication", methods=["POST"])
@login_required
def add_medication():
    """Handles adding medication and syncing with Google Calendar."""
    name = request.form["name"]
    dosage = request.form["dosage"]
    frequency = request.form["frequency"]
    reminder_time = datetime.strptime(request.form["reminder_time"], "%Y-%m-%dT%H:%M")

    medication = Medication(
        user_id=current_user.id,
        name=name,
        dosage=dosage,
        frequency=frequency,
        reminder_time=reminder_time.time()
    )

    db.session.add(medication)
    db.session.commit()

    # Sync with Google Calendar and store event ID
    event_id = add_medication_event(current_user.email, name, dosage, reminder_time)
    medication.event_id = event_id  # Store event ID in the database
    db.session.commit()

    flash("Medication added successfully!", "success")
    return redirect(url_for("dashboard"))

@app.route("/delete_medication/<int:med_id>", methods=["POST"])
@login_required
def delete_medication(med_id):
    medication = Medication.query.get_or_404(med_id)
    if medication.user_id != current_user.id:
        flash("Unauthorized action!", "danger")
        return redirect(url_for("dashboard"))

    # Remove from Google Calendar if event exists
    if medication.event_id:
        delete_medication_event(medication.event_id)

    db.session.delete(medication)
    db.session.commit()

    flash("Medication deleted successfully!", "success")
    return redirect(url_for("dashboard"))
