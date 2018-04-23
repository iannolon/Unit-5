(this was done in the console)

>>> #make a list with Monday, Tuesday, Wednesday
>>> week = ['Monday','Tuesday','Wednesday']
>>> week
['Monday', 'Tuesday', 'Wednesday']
>>> week[1]
'Tuesday'
>>> week[-2]
'Tuesday'
>>> week.append('Thursday')
>>> week
['Monday', 'Tuesday', 'Wednesday', 'Thursday']
>>> week[1:3]
['Tuesday', 'Wednesday']
>>> week.remove('Monday')
>>> week
['Tuesday', 'Wednesday', 'Thursday']
>>> week.sort()
>>> week
['Thursday', 'Tuesday', 'Wednesday']
>>> week.reverse()
>>> week
['Wednesday', 'Tuesday', 'Thursday']
>>> week[1]='Friday'
>>> week
['Wednesday', 'Friday', 'Thursday']
>>> len(week)
3
>>> 
