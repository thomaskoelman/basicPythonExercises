import datetime

now = datetime.datetime.now()
print("option 1: " + now.strftime("%Y-%m-%d %H:%M:%S"))
print("option 2:", now.date(), now.time().replace(microsecond=0), end=" ")
print("\noption 3:", now.replace(microsecond=0))
