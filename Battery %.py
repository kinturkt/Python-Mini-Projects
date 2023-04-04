import psutil

battery=psutil.sensors_battery()
percentage=battery.percent
print("My current battery % is", percentage)
print(f"My system has {percentage} percent battery left")