# -*- coding: UTF8 -*-

import numpy as np
with open("claims.txt", "r") as freq_file:
    content = freq_file.readlines()

x_max = 0
y_max = 0
claims = []

overlaps = set({})
for line in content:
    split_1 = line.split('@')
    id = int(split_1[0][1:-1])

    split_2 = split_1[1].split(':')
    pos = split_2[0]
    dims = split_2[1]

    x_pos = int(pos.split(',')[0])
    y_pos = int(pos.split(',')[1])

    width = int(dims.split('x')[0])
    height = int(dims.split('x')[1])

    # print ("#{} @ {},{}: {}x{}".format(id, x_pos, y_pos, width, height))

    claims.append({'id': id, 'x':x_pos, 'y':y_pos, 'width':width, 'height':height})

    if x_pos+width > x_max:
        x_max = x_pos+width

    if y_pos+height > y_max:
        y_max = y_pos+height

fabric = np.zeros((x_max, y_max))
# print len(np.nonzero(fabric > 1)[0])

for claim in claims:
    for x in range(claim['width']):
        for y in range(claim['height']):
            fabric[claim['x']+x] [claim['y']+y] = fabric[claim['x']+x] [claim['y']+y] + 1

print len(np.nonzero(fabric > 1)[0])
