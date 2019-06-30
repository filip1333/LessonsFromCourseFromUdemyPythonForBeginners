import time
import calendar

print(time.time())
print(time.localtime())
print(time.localtime(time.time()))
print(calendar.month(1988, 9))
calendar.setfirstweekday(6)
print(calendar.isleap(2000))
print(calendar.calendar(2019))
