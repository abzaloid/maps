import csv

res = []

with open('weighted_geopositions/kyzylorda_weighted.txt', 'rb') as csvfile:
    georeader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in georeader:
    	# res.append('{location: new google.maps.LatLng(%s, %s), weight: %s},'%(row[0],row[1],row[2]))
    	res.append('%s,%s,%s'%(row[0],row[1],row[2]))
f = open('weighted_geopositions_js/kyzylorda_js.txt', 'w')

for r in res:
	f.write(r+'\n')

f.close()