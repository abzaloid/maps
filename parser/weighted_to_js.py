import csv
import random

res = []

with open('weighted_geopositions/kyzylorda_weighted.txt', 'rb') as csvfile:
    georeader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in georeader:
    	res.append('{location: new google.maps.LatLng(%s, %s), weight: %s},'%(row[0],row[1],min(float(row[2]), 10.0)))
    	# res.append('%s,%s,%s'%(row[0],row[1],min(float(row[2]), 50)))
f = open('weighted_geopositions_js/kyzylorda_js.txt', 'w')

if len(res) > 1000:
	res = random.sample(res, 1000)

for r in res:
	f.write(r+'\n')

f.close()