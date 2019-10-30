import datetime
import pytz
import csv

#tday = datetime.date.today()

#tdelta = datetime.timedelta(days=7)

#print(tday - tdelta)

# date2 = date1 + timedelta
#timedelta = date1 + date2

#bday = datetime.date(1997, 1, 2)

#till_bday = bday - tday
#print(till_bday.total_seconds())

# dt_today = datetime.datetime.today()
# dt_now = datetime.datetime.now()
# dt_utcnow = datetime.datetime.utcnow()

#dt = datetime.datetime(2019, 2, 26, 12, 30, 45, tzinfo=pytz.UTC)
#print(dt)

dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
# print(dt_utcnow)

dt_ng = dt_utcnow.astimezone(pytz.timezone('Africa/Lagos'))
# print(dt_ng)

# dt_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
# print(dt_utcnow)

for tz in pytz.all_timezones:
    print(tz)
