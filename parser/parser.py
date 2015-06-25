import xml.etree.ElementTree as ET

tree = ET.parse('cities/kyzylorda.xml')
root = tree.getroot()