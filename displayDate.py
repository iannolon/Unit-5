#IanNolon
#4/26/28
#displayDate.py

from datetime import *
dotw = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'] #dotw = days of the week
weekday = dotw[today.weekday()]
today = date.today()
day = today.day
year = today.year


month = today.month
print('Today is',weekday,',',month,day,year)
