# This code is checking the battery percentage of the device and if it is less than or equal to 30%
# and the device is not plugged in, it sends a notification to the user using the `pynotifier`
# library. The notification includes the battery percentage and a message indicating that the battery
# is low.
# pip install psutil
import psutil
battery = psutil.sensors_battery()
plugged = battery.power_plugged
percent = battery.percent
if percent <= 30 and plugged!=True:
    
    # pip install py-notifier
    # pip install win10toast
    from pynotifier import Notification
    Notification(
        title="Battery Low",
        description=str(percent) + "% Battery remain!!",
        duration=5, # Duration in seconds
    
    ).send()
