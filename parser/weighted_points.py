from kdtree import KDTree

import csv

def get_dist(pointA, pointB):
	dist = 0.0
	for i in range(len(pointA)):
		dist += (pointA[i] - pointB[i]) * (pointA[i] - pointB[i])
	return dist


points = []

with open('geopositions/kyzylorda.txt', 'rb') as csvfile:
    georeader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in georeader:
        points.append((float(row[0]), float(row[1]), 1.0))

cnt = 0
while len(points) > 1000:
	print cnt
	cnt += 1
	tree = KDTree.construct_from_data(points)
	min_dist = 2000000000
	f_point = None
	s_point = None
	for point in points:
		nearest = tree.query(query_point=point, t=2)
		found_point = nearest[1]
		dist = get_dist(found_point, point)
		if dist < min_dist:
			f_point = found_point
			s_point = point
			min_dist = dist
	if f_point is not None:
		ind = 0
		for i in range(len(points)):
			if points[i] == f_point:
				ind = i
				break
		points = points[:ind] + points[ind+1:]
		ind = 0
		for i in range(len(points)):
			if points[i] == s_point:
				ind = i
				break
		points = points[:ind] + points[ind+1:]
		new_point = ((f_point[0]+s_point[0])/2,(f_point[1]+s_point[1])/2,(f_point[2]+s_point[2])/2)
		points.append(new_point)
	else:
		break


