
# coding=utf-8

import xml.etree.ElementTree as ET

tree = ET.parse('cities/kyzylorda.xml')
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

f = open('streets/kyzylorda.txt', 'w')
for street in street_data:
	f.write(street.encode('utf-8'))
	f.write('\n')
f.close()

f = open('geopositions/kyzylorda.txt', 'w')
for geoposition in geo_data:
	f.write(geoposition.encode('utf-8'))
	f.write('\n')
f.close()
