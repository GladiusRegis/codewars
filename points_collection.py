games0 = ['1:0', '2:0', '3:0', '4:0', '2:1', '3:1', '4:1', '3:2', '4:2', '4:3']  # 30
games1 = ['1:1', '2:2', '3:3', '4:4', '2:2', '3:3', '4:4', '3:3', '4:4', '4:4']  # 10
games2 = ['0:1', '0:2', '0:3', '0:4', '1:2', '1:3', '1:4', '2:3', '2:4', '3:4']  # 0
games3 = ['1:0', '2:0', '3:0', '4:0', '2:1', '1:3', '1:4', '2:3', '2:4', '3:4']  # 15
games4 = ['1:0', '2:0', '3:0', '4:4', '2:2', '3:3', '1:4', '2:3', '2:4', '3:4']  # 12


def counting_points(items):
    point = 0
    for item in items:
        if item[0] > item[-1]:
            point += 3
        elif item[0] < item[-1]:
            point += 0
        else:
            point += 1
    return point


print(counting_points(games0))
print(counting_points(games1))
print(counting_points(games2))
print(counting_points(games3))
print(counting_points(games4))


def points(a):
    return sum((x >= y) + 2 * (x > y) for x, y in (s.split(":") for s in a))


print(counting_points(games0))
print(counting_points(games1))
print(counting_points(games2))
print(counting_points(games3))
print(counting_points(games4))


def points(games):
    return sum([0, 1, 3][1 + (g[0] > g[2]) - (g[0] < g[2])] for g in games)


print(counting_points(games0))
print(counting_points(games1))
print(counting_points(games2))
print(counting_points(games3))
print(counting_points(games4))
