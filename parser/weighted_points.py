from kdtree import KDTree

import csv
import time
from sets import Set

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

block_size = 100
start_time = time.time()
while len(points) > 1000:
	print len(points)
	s_time = time.time()
	tree = KDTree.construct_from_data(points)
	# min_dist = 2000000000
	# f_point = None
	# s_point = None
	pairs = []
	for point in points:
		nearest = tree.query(query_point=point, t=2)
		found_point = nearest[1]
		dist = get_dist(found_point, point)
		pairs.append((point, found_point, dist))
		# if dist < min_dist:
		# 	f_point = found_point
		# 	s_point = point
		# 	min_dist = dist
	pairs.sort(key=lambda x: x[2])
	all_pairs = []
	used = Set()
	for pair in pairs:
		p_a = pair[0]
		p_b = pair[1]
		if p_a not in used and p_b not in used:
			used.add(p_a)
			used.add(p_b)
			all_pairs.append(pair)
			if len(all_pairs) == block_size:
				break
	# pairs = pairs[:block_size]
	pairs = all_pairs
	new_points = []
	for (f_point, s_point, dist) in pairs:
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
		new_points.append(((f_point[0]+s_point[0])/2,
							(f_point[1]+s_point[1])/2,
							(f_point[2]+s_point[2])/2))
	points+=new_points
	print time.time() - s_time

print 'total: ' + str(time.time() - start_time)

f = open('kyzylorda_weighted.txt', 'w')
for point in points:
	for d in point:
		f.write(unicode(d) + u',')
	f.write('\n')
f.close()
