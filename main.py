import calendar_functions
import med_reminders
import pharmacyinfo
import route

def main():
    # Initialize the app
    app = create_app()

    # Set up calendar functions
    calendar = calendar_functions.Calendar()
    calendar.setup()

    # Set up medication reminders
    reminders = med_reminders.Reminders()
    reminders.setup()

    # Set up pharmacy information
    pharmacy = pharmacyinfo.PharmacyInfo()
    pharmacy.setup()

    # Set up routes
    route.setup_routes(app)

    # Run the app
    app.run()

if __name__ == "__main__":
    main()
