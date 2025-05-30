import time
from plyer import notification

while True:
    print("Started")
    notification.notify(title="Drink Water", message="Stay Hydrated")
    time.sleep(3)


