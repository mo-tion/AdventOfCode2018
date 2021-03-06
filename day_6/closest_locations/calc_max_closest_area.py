import numpy as np
import sys

def l1_dist(p1, p2):
    return np.sum(np.abs(p1-p2))

with open("locations.txt", "r") as freq_file:
    locations_input = freq_file.readlines()

min_x = float('Inf')
max_x = 0
min_y = float('Inf')
max_y = 0

min_x_id = -1
min_y_id = -1

max_x_id = -1
max_y_id = -1

points = []
points_to_num_closest = {}
for i, point_input in enumerate(locations_input):
    x, y = point_input.split(',')
    x = int(x)
    y = int(y)

    if x < min_x:
        min_x = x
        min_x_id = i
    if x > max_x:
        max_x = x
        max_x_id = i
    if y < min_y:
        min_y = y
        min_y_id = i
    if y > max_y:
        max_y = y
        max_y_id = i

    points_to_num_closest[i] = 0

    points.append(np.array((x, y)))

inf_area_ids = set({})
for y in range(min_y-2, max_y+3):
    for x in range(min_x-2, max_x+3):
        min_dist = float('Inf')
        min_dist_id = -1
        dist_tied = False
        for i, point in enumerate(points):
            dist = l1_dist(point, np.array((x, y)))
            if dist == min_dist:
                dist_tied = True
            if dist < min_dist:
                min_dist = dist
                min_dist_id = i
                dist_tied = False
        
        if (not dist_tied):
            points_to_num_closest[min_dist_id] += 1

        if (x in list([min_x-2, max_x+2])) or (y in list([min_y-2, max_y+2])):
            inf_area_ids.add(min_dist_id)


#remove inf areas
filtered = list(filter(lambda x: x[0] not in inf_area_ids, points_to_num_closest.items()))

print ( max (filtered , key=lambda x: x[1]))
