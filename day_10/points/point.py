class Point:
    def __init__(self, x, y, vel_x, vel_y):
        self.x = x
        self.y = y
        self.vel_x = vel_x
        self.vel_y = vel_y

    def step(self):
        self.x += self.vel_x
        self.y += self.vel_y