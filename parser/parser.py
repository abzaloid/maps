import xml.etree.ElementTree as ET

tree = ET.parse('cities/kyzylorda.xml')
root = tree.getroot()

geo_data = []
street_data = []

for i in range(len(root)):
	for j in range(len(root[i])):
		if root[i][j].text is not None:
			if 'geoposition' in unicode(root[i][j]):
				geo_data.append(unicode(root[i][j].text))
				break
			if 'street' in unicode(root[i][j]):
				street_data.append(unicode(root[i][j].text))

f = open('street_data.txt', 'w')
for street in street_data:
	f.write(street.encode('utf-8'))

print len(geo_data)
print len(street_data)
print len(root)

