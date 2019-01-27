#Couting no of sunday in the year
'''
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?'''

from datetime import date
from collections import Counter
n=int(input())
days=['mon','tue','wed','thu','fri','sat','sun']
initial_year=1901
final_year=n
sunday_count=0
day_left=1
while initial_year<=final_year:
	first_day=days[day_left]
	sunday_year=0	
	#for leap year
	if (initial_year%4==0 and initial_year%100!=0) or (initial_year%100==0 and initial_year%400==0):
		day_left+=2
		if first_day in ['mon','wed','thu']:
			sunday_year+=2
		elif first_day=='sun':
			sunday_year+=3
		else:
			sunday_year+=1
	else:
		if first_day in ['mon','tue','sun']:
			sunday_year+=2
		elif first_day=='thu':
			sunday_year+=3
		else:
			sunday_year+=1
		day_left+=1
	if day_left>=7:
		day_left+=-7
	sunday_count+=sunday_year
	initial_year+=1
	
print(sunday_count)



counter = Counter()

for year in range(1901, 2001):
    for month in range(1, 13):
        day = date(year, month, 1)
        counter[day.weekday()] += 1

print (counter[6])

