# Write a Python program to compute the distance between the points (x1, y1) and (x2, y2).
import math
def dist(x1, y1 ,x2, y2):
    xdis = x2 - x1
    ydis = y2 - y1

    distance = math.sqrt(xdis**2 + ydis**2)
    return distance

print (dist(4, 0, 6, 6))