
# coding=utf-8

import xml.etree.ElementTree as ET
from sets import Set

from getfiles import files

for city in files:

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

	unique = Set(geo_data)
	geo_data = []
	for el in unique:
		geo_data.append(el)
	f = open('geopositions/'+city_name+'.txt', 'w')
	for geoposition in geo_data:
		f.write(geoposition.encode('utf-8'))
		f.write('\n')
	f.close()
