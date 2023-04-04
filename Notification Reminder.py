import time
from plyer import notification
if __name__=='__main__':
    while True:
        notification.notify(
            title="All Day Reminder",
            message="Today you have to submit my assignment but have not completed it till now",
            timeout=15
        )
        time.sleep(60*60)