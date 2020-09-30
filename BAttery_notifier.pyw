import psutil
import os

battery = psutil.sensors_battery()

percent = battery.percent

from win10toast import ToastNotifier

toaster = ToastNotifier()

icon = os.path.join('/programming folder/python/practise/BAttery_notifier/','pro.ico')
print(icon)


while toaster.notification_active(): time.sleep(0.01)

if percent <50:
    toaster.show_toast("Battery Notifier",f"Your battery percent is {percent}%" + "\n" + "Please Charge" ,duration = 10 ,icon_path = icon)
    
elif percent >= 85:
    toaster.show_toast("Battery Notifier",f"Your battery percent is {percent}%" + "\n" + "Please take out the cahrger",duration = 10,icon_path = icon)

elif percent < 30:
    toaster.show_toast("Battery Notifier",f"Your battery percent is getting low Please Charge",duration = 10 ,icon_path = icon)

toaster.show_toast("Battery Notifier",f"Your battery percent is {percent}%" + "\n" + "Please Charge" ,duration = 10 ,icon_path = icon)
