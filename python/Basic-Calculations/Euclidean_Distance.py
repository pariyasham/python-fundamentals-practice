# Given two points:
# Point 1: (x1 = 5, y1 = 4)
# Point 2: (x2 = 3, y2 = 2)
# Using the Euclidean distance formula, calculate and print the distance
# between these two points using Python.

import math

points_1 = (5,4)
points_2 = (3,2)


euclidean_distance = math.sqrt(((points_2[0] - points_1[0])**2) + ((points_2[1] - points_1[1])**2))

print(f"• Point 1: {points_1}")
print(f"• Point 2: {points_2}")
print(f"• Euclidean Distance: {euclidean_distance: .2f}")