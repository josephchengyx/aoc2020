from copy import deepcopy

with open('day17_input.txt', newline='') as f:
    reader = f.read().splitlines()
    data = list()
    for line in reader:
        data.append(list(line))

part_1_data = [data]

def print_arr(arr):
    z = 0 - int(len(arr)//2)
    for plane in arr:
        print(f'z = {z}')
        for row in plane:
            print(row)
        z += 1
        print('')

# print_arr(part_1_data)



def change_state(arr, x, y, z):
    X, Y, Z = len(arr[z][y]), len(arr[z]), len(arr)
    cube = arr[z][y][x]

    active = 0
    for k in range(z-1, z+2):
        for j in range(y-1, y+2):
            for i in range(x-1, x+2):
                if (i < 0 or i > X-1) or (j < 0 or j > Y-1) or (k < 0 or k > Z-1) or (i == x and j == y and k == z):
                    continue
                if arr[k][j][i] == '#':
                    active += 1
    
    if cube == '#':
        return False if active == 2 or active == 3 else True
    else:
        return True if active == 3 else False

def expand_arr(arr):
    X, Y = len(arr[0][0]) + 2, len(arr[0]) + 2
    for plane in arr:
        for row in plane:
            row.insert(0, '.')
            row.append('.')

        plane.insert(0, ['.' for i in range(X)])
        plane.append(['.' for i in range(X)])
    
    arr.insert(0, [['.' for i in range(X)] for j in range(Y)])
    arr.append([['.' for i in range(X)] for j in range(Y)])

    return arr

def part_1(data, cycles):
    prev, curr = deepcopy(data), deepcopy(data)
    for n in range(cycles):
        prev, curr = expand_arr(prev), expand_arr(curr)
        X, Y, Z = len(prev[0][0]), len(prev[0]), len(prev)

        for k in range(Z):
            for j in range(Y):
                for i in range(X):
                    if change_state(prev, i, j, k):
                        if prev[k][j][i] == '#':
                            curr[k][j][i] = '.'
                        else:
                            curr[k][j][i] = '#'
            
        prev = deepcopy(curr)
    
    X, Y, Z = len(prev[0][0]), len(prev[0]), len(prev)
    active = 0
    for k in range(Z):
        for j in range(Y):
            for i in range(X):
                if prev[k][j][i] == '#':
                    active += 1
    
    return active



ans_1 = part_1(part_1_data, 6)
print(f'Part 1: {ans_1}')