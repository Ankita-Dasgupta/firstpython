import calendar
date = int(input("enter the day"))
month = int(input("enter the month"))
year = int(input("enter the year"))

dd = (calendar.weekday(year, month, date))
x = calendar.day_name[dd]
print(x)

