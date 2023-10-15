# Forrest's Run

import math

def calculate_distance(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

def minimum_distance_route(points):
    points.sort(key=lambda point: point[0])
    leftmost_point = points[0]
    rightmost_point = points[-1]

    above_line_points = []
    below_line_points = []

    for point in points[1:-1]:
        # Determine the position of the point relative to the line
        line_slope = (rightmost_point[1] - leftmost_point[1]) / (rightmost_point[0] - leftmost_point[0])
        line_intercept = leftmost_point[1] - line_slope * leftmost_point[0]
        if point[1] > line_slope * point[0] + line_intercept:
            above_line_points.append(point)
        else:
            below_line_points.append(point)

    # Sort the points in each group based on the x-coordinate
    above_line_points.sort(key=lambda point: point[0])
    below_line_points.sort(key=lambda point: point[0])

    # Calculate the total distance
    total_distance = 0
    current_point = leftmost_point
    for point in above_line_points + [rightmost_point] + below_line_points[::-1]:
        total_distance += calculate_distance(current_point, point)
        current_point = point
    total_distance += calculate_distance(current_point, leftmost_point)  # Return to the starting point

    return total_distance

n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
distance = minimum_distance_route(points)
print(f'{distance:.2f}')
