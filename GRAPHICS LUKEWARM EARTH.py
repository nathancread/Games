import pygame
import random
import os
import math

# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BROWN    = ( 43,   23,  13)
BLUE     = ( 0,     0,  225)
ORANGE   = (250, 133,  0)
pygame.init()

#bottom is actually side 
BOTTOM = 90
#side is acually bottom
SIDE = 150
point_array = [0,70 , 15,62 , 50,62 , 75,80 , 120,85 , 150,85]
dirt_list =  [[0 for ii in range(SIDE+1)] for jj in range (BOTTOM+1)]
for x in range(SIDE+1):
    for y in range (BOTTOM+1):
        if x <= point_array[2] and x >= point_array[0]:
            if y >= point_array[3] and y >= point_array[1] :
                m = (point_array[3] - point_array[1])/(point_array[2] - point_array[0])
                b = (m * point_array[0])- point_array[1]
                if y >= m * x - b :
                    dirt_list[x][y] = 1
                    print(x,y)
                    
        if x <= point_array[4] and x >= point_array[2]:
            if y >= point_array[5] and y >= point_array[3] :
                m = (point_array[5] - point_array[3])/(point_array[4] - point_array[2])
                b = (m * point_array[2])- point_array[3]
                if y >= m * x - b :
                    dirt_list[x][y] = 1
                    print("---")
                    print(x,y)
                    
        if x <= point_array[6] and x >= point_array[4]:
            if y >= point_array[7] and y >= point_array[5] :
                m = (point_array[7] - point_array[5])/(point_array[6] - point_array[4])
                b = (m * point_array[4])- point_array[5]
                if y >= m * x - b :
                    dirt_list[x][y] = 1
                    print("+++")
                    print(x,y)

        if x <= point_array[8] and x >= point_array[6]:
            if y >= point_array[9] and y >= point_array[7] :
                m = (point_array[9] - point_array[7])/(point_array[8] - point_array[6])
                b = (m * point_array[6])- point_array[7]
                if y >= m * x - b :
                    dirt_list[x][y] = 1
                    print("...")
                    print(x,y)

        if x <= point_array[10] and x >= point_array[8]:
            if y >= point_array[11] and y >= point_array[9] :
                m = (point_array[11] - point_array[9])/(point_array[10] - point_array[8])
                b = (m * point_array[8])- point_array[9]
                if y >= m * x - b :
                    dirt_list[x][y] = 1
                    print("###")
                    print(x,y)

