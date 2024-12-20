import matplotlib.pyplot as plt
import numpy as np

def orientation(a, b, c, epsilon=1e-9):
    ax, ay = a
    bx, by = b
    cx, cy = c
    val = (bx - ax) * (cy - ay) - (cx - ax) * (by - ay)
    if abs(val) < epsilon:
        return 0  # Collinear
    return 1 if val > 0 else -1  # 1 CCW -1 CW


def distance(a, b):
    ax, ay = a
    bx, by = b
    return (bx - ax) ** 2 + (by - ay) ** 2


def leftMostPoint( intersections):
    min = 0
    for i in range(1, len(intersections)):
        inter_x, inter_y = intersections[i]
        min_x, min_y = intersections[min]
        if inter_x < min_x:
            min = i
        elif inter_x == min_x and inter_y > min_y:
            min = i
    return min

def polar_angle(p0, p):
    angle = np.arctan2(p[1] - p0[1], p[0] - p0[0])
    dist = distance(p0, p)
    return (angle, dist)
def GrahamsScan(points):
    min = leftMostPoint(points)
    p0 = points[min]
    # sort based on polar angle in counterclockwise order around p0
    sorted_points = sorted(points, key=lambda p:polar_angle(p0, p))
    hull = [p0, sorted_points[0], sorted_points[1]]
    for point in sorted_points:
        while len(hull) >= 2 and orientation(hull[-2], hull[-1], point) != 1:
            hull.pop()
        hull.append(point)
    return hull


def visualize_convex_hull(points):
    convex_hull=GrahamsScan(points)
    convex_hull.append(convex_hull[0])
    x_points, y_points = zip(*points)
    x_hull, y_hull = zip(*convex_hull)
    plt.figure(figsize=(8, 6))
    plt.scatter(x_points, y_points, color='blue', label='Points')
    plt.plot(x_hull, y_hull, color='red', label='Convex Hull', linestyle='-', marker='o')
    plt.title("Convex Hull Visualization")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.grid(True)
    plt.show()

points=[(1,1),(4,3),(4,7),(5,3),(10,4),(10,6),(11,7),(13,1),(13,8)]
visualize_convex_hull(points)
convex_hull=GrahamsScan(points)
print(convex_hull)
