import csv
from copy import deepcopy

with open('day11_input.csv', newline='') as f:
    reader = csv.reader(f)
    data = list()
    for line in reader:
        line = list(line[0])
        data.append(line)

# def print_arr(arr):
#     for row in arr:
#         print(row)

# print_arr(data[:5])



def part_1(data, x, y):
    X, Y = len(data[0]), len(data)
    seat = data[y][x]
    if seat == '.':
        return False
    
    occ = 0
    for j in range(y-1, y+2):
        for i in range(x-1, x+2):
            if (i < 0 or i > X-1) or (j < 0 or j > Y-1) or (i == x and j == y):
                continue
            if data[j][i] == '#':
                if seat == 'L':
                    return False
                occ += 1
                if occ >= 4:
                    return True
    
    return True if seat == 'L' else False



def part_2(data, x, y):
    X, Y = len(data[0]), len(data)
    seat = data[y][x]
    if seat == '.':
        return False

    xi, yi = x, y
    occ = 0

    while x >= 0 and y >= 0:   # diag up, left
        if x == xi and y == yi:
            pass
        elif data[y][x] == '#':
            if seat == 'L':
                return False
            occ += 1
            if occ >= 5:
                return True
            break
        elif data[y][x] == 'L':
            break
        x -= 1
        y -= 1
    x, y, = xi, yi

    while y >= 0:   # up
        if x == xi and y == yi:
            pass
        elif data[y][x] == '#':
            if seat == 'L':
                return False
            occ += 1
            if occ >= 5:
                return True
            break
        elif data[y][x] == 'L':
            break
        y -= 1
    y = yi

    while x <= X-1 and y >= 0:   # diag up, right
        if x == xi and y == yi:
            pass
        elif data[y][x] == '#':
            if seat == 'L':
                return False
            occ += 1
            if occ >= 5:
                return True
            break
        elif data[y][x] == 'L':
            break
        x += 1
        y -= 1
    x, y, = xi, yi

    while x >= 0:   # left
        if x == xi and y == yi:
            pass
        elif data[y][x] == '#':
            if seat == 'L':
                return False
            occ += 1
            if occ >= 5:
                return True
            break
        elif data[y][x] == 'L':
            break
        x -= 1
    x = xi

    while x <= X-1:   # right
        if x == xi and y == yi:
            pass
        elif data[y][x] == '#':
            if seat == 'L':
                return False
            occ += 1
            if occ >= 5:
                return True
            break
        elif data[y][x] == 'L':
            break
        x += 1
    x = xi

    while x >= 0 and y <= Y-1:   # diag down, left
        if x == xi and y == yi:
            pass
        elif data[y][x] == '#':
            if seat == 'L':
                return False
            occ += 1
            if occ >= 5:
                return True
            break
        elif data[y][x] == 'L':
            break
        x -= 1
        y += 1
    x, y, = xi, yi

    while y <= Y-1:   # down
        if x == xi and y == yi:
            pass
        elif data[y][x] == '#':
            if seat == 'L':
                return False
            occ += 1
            if occ >= 5:
                return True
            break
        elif data[y][x] == 'L':
            break
        y += 1
    y = yi

    while x <= X-1 and y <= Y-1:   # diag down, right
        if x == xi and y == yi:
            pass
        elif data[y][x] == '#':
            if seat == 'L':
                return False
            occ += 1
            if occ >= 5:
                return True
            break
        elif data[y][x] == 'L':
            break
        x += 1
        y += 1

    return True if seat == 'L' else False



def shifting_seats(data, check):
    layout = deepcopy(data)
    edits = deepcopy(layout)
    X, Y = len(layout[0]), len(layout)

    swap = True
    while swap:
        swap = False
        for j in range(Y):
            for i in range(X):
                if check(layout, i, j):
                    if layout[j][i] == 'L':
                        edits[j][i] = '#'
                    elif layout[j][i] == '#':
                        edits[j][i] = 'L'
                    swap = True
        layout = deepcopy(edits)
    
    occ = 0
    for j in range(Y):
        for i in range(X):
            if layout[j][i] == '#':
                occ += 1
    return occ



ans_1 = shifting_seats(data, part_1)
ans_2 = shifting_seats(data, part_2)
print(f'Part 1: {ans_1}')
print(f'Part 2: {ans_2}')