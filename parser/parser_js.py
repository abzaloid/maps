
# coding=utf-8

import xml.etree.ElementTree as ET
import random

from os import listdir
from os.path import isfile, join

# mypath = 'cities/'
# onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]

# print onlyfiles

onlyfiles = ['kyzylorda.xml']

for city in onlyfiles:

	print city

	city_name = city.split('.')[0]

	print city_name

	tree = ET.parse('cities/' + city)
	root = tree.getroot()
	geo_data = []
	street_data = []

	for i in range(len(root)):
		for j in range(len(root[i])):
			if root[i][j].text is not None:
				if 'geoposition' in unicode(root[i][j]):
					geo_data.append(unicode(root[i][j].text).lstrip())
					break
				if 'street' in unicode(root[i][j]) and not u'НЕИЗВЕСТНАЯ' in unicode(root[i][j].text):
					street_data.append(unicode(root[i][j].text).lstrip())

	f = open('streets/'+city_name+'.txt', 'w')
	for street in street_data:
		f.write(street.encode('utf-8'))
		f.write('\n')
	f.close()

	f = open('geopositions/'+city_name+'.txt', 'w')
	geo_data = random.sample(geo_data, 400)
	for geoposition in geo_data:
		f.write(u'new google.maps.LatLng(%s),'%(geoposition.encode('utf-8')))
		f.write('\n')

	f.close()
