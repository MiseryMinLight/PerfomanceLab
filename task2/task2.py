import sys
import math

if len(sys.argv) != 3:
    print("Хочу два файла")
    sys.exit(1)

ellipse_file = sys.argv[1]
points_file = sys.argv[2]

with open(ellipse_file, "r") as file:
    center = file.readline().split()
    radius = file.readline().split()

x0 = float(center[0])
y0 = float(center[1])

a = float(radius[0])
b = float(radius[1])

def check_point(x, y):
    result = ((x - x0) ** 2 / a ** 2) + ((y - y0) ** 2 / b ** 2)

    if math.isclose(result, 1.0, rel_tol=1e-9, abs_tol=1e-12):
        return 0
    elif result < 1:
        return 1
    else:
        return 2

with open(points_file, "r") as file:
    for line in file:
        point = line.split()

        x = float(point[0])
        y = float(point[1])

        position = check_point(x, y)

        print(position)

print("эллипс:", ellipse_file)
print("точки:", points_file)