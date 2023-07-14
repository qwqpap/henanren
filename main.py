# This is a sample Python script.
import time
import numpy as np
import random
import math
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.use('TkAgg')
class Location:
    def __init__(self,left_location,right_location):
        self.wheelbase = 10
        self.radius = 5
        self.last_left_location = left_location
        self.last_right_location = right_location
        self.now_location = [0,0]
        self.now_dig = 0

    def dig_config(self):
        if self.now_dig > math.pi:
            self.now_dig = self.now_dig - 2 * math.pi
        elif self.now_dig < -math.pi:
            self.now_dig = self.now_dig + 2 * math.pi
        else:
            pass
        # 旨在确保角度的区间不会起飞


    def count_location(self,left_now,right_now):
        delta_left = left_now - self.last_left_location
        delta_right = right_now - self.last_right_location
        self.last_left_location = left_now
        self.last_right_location = right_now
        # 计算和上次的差值
        dist_right = delta_right * self.radius
        dist_left = delta_left * self.radius
        dis = (dist_left + dist_right)/2
        # 计算大概的走的距离
        dig = math.atan((dist_right - dist_left)/self.wheelbase)
        return (self.flash_location(dig,dis))

    def flash_location(self,dig_add,dis_add):
        self.now_dig += dig_add
        self.dig_config()
        #print(self.now_dig)

        x_delta = math.cos(self.now_dig)*dis_add
        y_delta = math.sin(self.now_dig)*dis_add
        #print(dig_add)
        self.now_location[0] = self.now_location[0] + x_delta
        self.now_location[1] = self.now_location[1] + y_delta

        return (self.now_location)
if __name__ == '__main__':
    loc = Location(0,0)
    a = 1
    b = 1
    js = 1
    x_list = []
    y_list = []
    loc_list = []
    while js <= 100000:
        #time.sleep(0.001)
        a += 0.001*random.random()
        b += 0.001*random.random()
        loc_list = loc.count_location(a,b)
        x_list.append( loc_list[0])
        y_list.append(loc_list[1])

        js = js + 1
    plt.plot(x_list,y_list)
    plt.show()

# now it`s finally working