import numpy as np
from scipy import signal

serial_number = 7672
grid_size = 300

power_grid = np.zeros([grid_size,grid_size])

for x in range(grid_size):
    for y in range(grid_size):
        rack_id = x+11
        power_level = rack_id*(y+1)
        power_level += serial_number
        power_level *= rack_id
        power_level = int(str(int(power_level/100))[-1])
        power_level -= 5
        power_grid[x,y] = power_level


max_power = float("-inf")
for size in range(1,grid_size+1):
    corr = signal.correlate2d(power_grid, np.ones([size,size]), boundary='fill', mode='valid')
    this_max = np.max(corr)
    if this_max > max_power:
        best_index = (str(np.unravel_index(np.argmax(corr), corr.shape))[1:-1])
        best_size = size
        max_power = this_max

print (best_index+", {}".format(best_size))