import csv
import random

from getfiles import files

all_data = []
res = []

for city in files:
	city_name = city.split('.')[0]


	cur_data = []

	with open('weighted_geopositions/%s_weighted.txt' % city_name, 'rb') as csvfile:
	    georeader = csv.reader(csvfile, delimiter=',', quotechar='|')
	    for row in georeader:
	    	cur_data.append(row)
	    	# res.append('{location: new google.maps.LatLng(%s, %s), weight: %s},'%(row[0],row[1],min(float(row[2]), 65.0)))
	    	# res.append('%s,%s,%s'%(row[0],row[1],min(float(row[2]), 50)))

	cur_data.sort(key=lambda x: x[2])
	all_data += cur_data[:-40]

f = open('all_data_js.txt', 'w')

for row in all_data:
	res.append('{location: new google.maps.LatLng(%s, %s), weight: %s},'%(row[0],row[1], row[2]))


for r in res:
	f.write(r+'\n')

f.close()

f = open('all_data.txt', 'w')

for r in all_data:
	for p in r:
		f.write(p+' ')
	f.write('\n')

f.close()