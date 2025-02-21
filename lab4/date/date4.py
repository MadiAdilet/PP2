import datetime
d1='2025-01-01'
d2='2025-02-21'
date_format = '%Y-%m-%d'
day1=datetime.datetime.strptime(d1,date_format)
day2=datetime.datetime.strptime(d2,date_format)
difference=day2-day1
print(difference)