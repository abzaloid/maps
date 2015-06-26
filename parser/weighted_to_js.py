import csv
import random

from getfiles import files

for city in files:
	city_name = city.split('.')[0]

	res = []

	with open('weighted_geopositions/%s_weighted.txt' % city_name, 'rb') as csvfile:
	    georeader = csv.reader(csvfile, delimiter=',', quotechar='|')
	    for row in georeader:
	    	res.append('{location: new google.maps.LatLng(%s, %s), weight: %s},'%(row[0],row[1],min(float(row[2]), 10000.0)))
	    	# res.append('%s,%s,%s'%(row[0],row[1],min(float(row[2]), 50)))
	f = open('weighted_geopositions_js/%s_js.txt' % city_name, 'w')

	max_points = 600

	if len(res) > max_points:
		res = random.sample(res, max_points)

	for r in res:
		f.write(r+'\n')

	f.close()