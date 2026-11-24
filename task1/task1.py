import sys


n1 = int(sys.argv[1])
m1 = int(sys.argv[2])

n2 = int(sys.argv[3])
m2 = int(sys.argv[4])

print("n1 =",n1)
print("m1 =",m1)
print("n2 =",n2)
print("m2 =",m2)

def get_path(n, m):
    index = 0
    path = []

    while True:
        path.append(str(index + 1))

        index = (index + m - 1) % n

        if index == 0:
            break

    return "".join(path)

path1 = get_path(n1, m1)
path2 = get_path(n2, m2)

print(path1 + path2)