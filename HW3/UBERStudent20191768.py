#!/usr/bin/python3
import sys
import datetime
def get_days(date):
	d = date.split('/')
	days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
	return days[datetime.date(int(d[2]),int(d[0]),int(d[1])).weekday()]
sys.stdout = open(sys.argv[2],'w')
result = {}
with open(sys.argv[1]) as file:
    for line in file:
    	data = line.strip().split(',')
    	print("{},{} {},{}".format(data[0], get_days(data[1]), data[2], data[3]))
sys.stdout.close()
