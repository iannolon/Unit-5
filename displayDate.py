#IanNolon
#4/26/28
#displayDate.py

from datetime import *
dotw = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'] #dotw = days of the week
moty = ['January','February','March','April','May','June','July','August','September','October','November','December'] #moty = months of the year
today = date.today()
weekday = dotw[today.weekday()]
month = today.month
month = moty[month-1]
day = today.day
year = today.year

print('Today is',weekday,',',month,day,year)
