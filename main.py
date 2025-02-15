from apscheduler.schedulers.background import BackgroundScheduler
import time

def send_reminder():
    print("Time to take your medication!")

if __name__ == "__main__":
    scheduler = BackgroundScheduler()
    scheduler.add_job(send_reminder, 'interval', hours=8)  # Adjust interval as needed
    scheduler.start()

    try:
        # Keep the script running
        while True:
            time.sleep(2)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
