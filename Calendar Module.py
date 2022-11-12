# Enter your code here. Read input from STDIN. Print output to STDOUT

import calendar
data = input().strip().split()
mm = data[0]
mm = int(mm)
dd = data[1]
dd = int(dd)
yy = data[2]
yy = int(yy)
dia = calendar.weekday(yy, mm, dd)
print(calendar.day_name[dia].upper())
