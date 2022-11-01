#!/usr/bin/python3
import sys
sys.stdout = open(sys.argv[2],'w')
genre = list()
result = {}
with open(sys.argv[1]) as file:
    for line in file:
    	data = line.strip().split('::')
    	genres = data[2].split('|')
    	for genre in genres:
    		if genre in result.keys():
    			result[genre] += 1
    		else:
    			result[genre] = 1
for k, v in result.items():
	print("{} {}".format(k, v))
sys.stdout.close()
