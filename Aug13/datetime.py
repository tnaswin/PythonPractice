from datetime import datetime

now = datetime.now()
print now.year
print now.month
print now.day

print '%02d/%02d/%02d %02d:%02d:%04d' % (now.month, now.day, now.year, 
					now.hour, now.minute, now.second)
