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
    	data[1] = get_days(data[1])
    	data[2] = int(data[2])
    	data[3] = int(data[3])
    	if len(result) == 0:
    		result[(data[0], data[1])] = [data[2],data[3]]
    	else:
    		if (data[0], data[1]) in result.keys():
    			temp = result[(data[0], data[1])]
    			temp[0] += data[2]
    			temp[1] += data[3]
    			result[(data[0], data[1])]= temp
    		else:
    			result[(data[0], data[1])] = [data[2],data[3]]
for k, v in result.items():
	print("{},{} {},{}".format(k[0], k[1], v[0], v[1]))
sys.stdout.close()
