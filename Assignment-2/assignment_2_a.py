# -*- coding: utf-8 -*-
"""Assignment_2_A.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14Kd6gKITn4shMwXeqHzUgBW-W0HnleEC
"""

import numpy as np
import matplotlib.pyplot as plt
import math

n = 100000
hit = 0

hit_x = []
hit_y = []

miss_x = []
miss_y = []

for i in range(n):
    x = np.random.uniform(low=0.0, high=3.0)
    y = np.random.uniform(low=0.0, high=2.0)
    if x>=0 and x <=1:
      if y<= x : 
        hit+=1
        hit_x.append(x)
        hit_y.append(y)
      else:
        miss_x.append(x)
        miss_y.append(y)
      
    else: 
      if y>=1 and y<=math.sqrt(1-(x-2)**2)+1 :
        hit+=1
        hit_x.append(x)
        hit_y.append(y)
      else: 
        miss_x.append(x)
        miss_y.append(y)
    
      
 
area = (hit/n)*6
print(area)
plt.scatter(hit_x, hit_y, c="red")
plt.scatter(miss_x, miss_y, c="green")
plt.show()