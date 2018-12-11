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

corr = signal.correlate2d(power_grid, np.ones([3,3]), boundary='fill', mode='valid')
print (str(np.unravel_index(np.argmax(corr), corr.shape))[1:-1])