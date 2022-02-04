# Author: Kimberly Rojas
# GitHub username: kimberlyroj
# Date: 2/3/2022
# Description:
class Taxicab():
    def __init__(self, x, y):
        self.x_coord = x
        self.y_coord = y
        self.odometer = 0

    def get_x_coord(self):
        return self.x_coord

    def get_y_coord(self):
        return self.y_coord

    def get_odometer(self):
        return self.odometer

    def move_x(self, distance):
        self.x_coord += distance
        self.odometer += abs(distance)

    def move_y(self, distance):
        self.y_coordinate += distance
        self.odometer += abs(distance)


