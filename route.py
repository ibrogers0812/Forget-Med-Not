# app/routes.py

from app import app
from flask import render_template

@app.route('/')
def home():
    return "Welcome to the Medication Reminder App!"

@app.route('/reminder')
def reminder():
    return "Time to take your medication!"
