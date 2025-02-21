import datetime
d=datetime.date.today()
y=d-datetime.timedelta(1)
t=d+datetime.timedelta(1)
print("Yesterday:",y)
print("Today:",d)
print("Tomorrow:",t)