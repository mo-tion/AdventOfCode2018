from point import Point
import cv2
import numpy as np

with open("initial_points.txt", "r") as input_file:
    file_content = input_file.readlines()

# file_content = [
# "position=< 9,  1> velocity=< 0,  2>",
# "position=< 7,  0> velocity=<-1,  0>",
# "position=< 3, -2> velocity=<-1,  1>",
# "position=< 6, 10> velocity=<-2, -1>",
# "position=< 2, -4> velocity=< 2,  2>",
# "position=<-6, 10> velocity=< 2, -2>",
# "position=< 1,  8> velocity=< 1, -1>",
# "position=< 1,  7> velocity=< 1,  0>",
# "position=<-3, 11> velocity=< 1, -2>",
# "position=< 7,  6> velocity=<-1, -1>",
# "position=<-2,  3> velocity=< 1,  0>",
# "position=<-4,  3> velocity=< 2,  0>",
# "position=<10, -3> velocity=<-1,  1>",
# "position=< 5, 11> velocity=< 1, -2>",
# "position=< 4,  7> velocity=< 0, -1>",
# "position=< 8, -2> velocity=< 0,  1>",
# "position=<15,  0> velocity=<-2,  0>",
# "position=< 1,  6> velocity=< 1,  0>",
# "position=< 8,  9> velocity=< 0, -1>",
# "position=< 3,  3> velocity=<-1,  1>"
# "position=< 0,  5> velocity=< 0, -1>",
# "position=<-2,  2> velocity=< 2,  0>"
# "position=< 5, -2> velocity=< 1,  2>",
# "position=< 1,  4> velocity=< 2,  1>"
# "position=<-2,  7> velocity=< 2, -2>",
# "position=< 3,  6> velocity=<-1, -1>",
# "position=< 5,  0> velocity=< 1,  0>",
# "position=<-6,  0> velocity=< 2,  0>",
# "position=< 5,  9> velocity=< 1, -2>",
# "position=<14,  7> velocity=<-2,  0>",
# "position=<-3,  6> velocity=< 2, -1>"
# ]

max_x = float("-inf")
max_y = float("-inf")

min_x = float("inf")
min_y = float("inf")

points = []

for point_line in file_content:
    x, y = point_line[point_line.find('<', 7)+1:point_line.find('>', 7)].split (',')
    x = int(x)
    y = int(y)

    if x < min_x:
        min_x = x

    if x > max_x:
        max_x = x

    if y < min_y:
        min_y = y

    if y > max_y:
        max_y = y

    vel_x, vel_y = point_line[point_line.find('<', 25)+1:point_line.find('>', 25)].split (',')
    vel_x = int(vel_x)
    vel_y = int(vel_y)

    # print ( "x: {}, y: {}, vel_x: {}, vel_y: {}".format(x, y, vel_x, vel_y) )
    points.append(Point(x, y, vel_x, vel_y))

print ("min_x: {}, max_x: {}".format(min_x, max_x))
print ("min_y: {}, max_y: {}".format(min_y, max_y))

res = 700
img = np.zeros((res, res, 1), np.uint8)

sim_time_low = 10904

for _ in range(sim_time_low):
    for point in points:
        point.step()

step_size = 1

step = 0

max_x = 250
max_y = 250
min_x = 100
min_y = 100

while (True):
    # print ("draw frame")
    img[:,:,:] = 0

    for _ in range(step_size):
        for point in points:
            point.step()

    for point in points:
        # print ("x: {}, y: {}".format(point.x, point.y))
        norm_x = float(point.x-min_x)/float(max_x-min_x)
        norm_y = float(point.y-min_y)/float(max_y-min_y)
        # print (norm_x, norm_y)
        draw_point_x = max(min(int(norm_x*(res-1)), res-1), 0)
        draw_point_y = max(min(int(norm_y*(res-1)), res-1), 0)
        # print (draw_point_x, draw_point_y)
        img[draw_point_y, draw_point_x] = 255
        
    cv2.imshow("img",img)
    cv2.waitKey(0)
    print ("frame: {}".format(sim_time_low+step*step_size))
    print ("min_x {}, max_x {}".format(min_x, max_x))
    print ("min_y {}, max_y {}".format(min_y, max_y))
    step += 1