import time

timestamp =int(time.strftime('%H'))
print(timestamp)
if timestamp<12:
    print("Good Morning!!")
elif timestamp>=12 and timestamp<=16:
    print("Good Afternoon!!")
elif timestamp>16 and timestamp<19:
    print("Good Evening!!")
else:
    print("Good nigh!!")