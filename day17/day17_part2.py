from copy import deepcopy

with open('day17_input.txt', newline='') as f:
    reader = f.read().splitlines()
    data = list()
    for line in reader:
        data.append(list(line))

part_2_data = [[data]]

# def print_arr(arr):
#     w = 0 - int(len(arr)//2)
#     for vol in arr:
#         z = 0 - int(len(arr[0])//2)
#         for plane in vol:
#             print(f'z = {z}, w = {w}')
#             for row in plane:
#                 print(row)
#             z += 1
#             print('')
#         w += 1  
#         print('\n')

# print_arr(data)



def change_state_v2(arr, x, y, z, w):
    X, Y, Z, W = len(arr[w][z][y]), len(arr[w][z]), len(arr[w]), len(arr)
    cube = arr[w][z][y][x]

    active = 0
    for h in range(w-1, w+2):
        for k in range(z-1, z+2):
            for j in range(y-1, y+2):
                for i in range(x-1, x+2):
                    if (i < 0 or i > X-1) or (j < 0 or j > Y-1) or (k < 0 or k > Z-1) or (h < 0 or h > W-1) or (i == x and j == y and k == z and h == w):
                        continue
                    if arr[h][k][j][i] == '#':
                        active += 1
    
    if cube == '#':
        return False if active == 2 or active == 3 else True
    else:
        return True if active == 3 else False

def expand_arr_v2(arr):
    X, Y, Z = len(arr[0][0][0]) + 2, len(arr[0][0]) + 2, len(arr[0]) + 2
    for vol in arr:
        for plane in vol:
            for row in plane:
                row.insert(0, '.')
                row.append('.')

            plane.insert(0, ['.' for i in range(X)])
            plane.append(['.' for i in range(X)])
    
        vol.insert(0, [['.' for i in range(X)] for j in range(Y)])
        vol.append([['.' for i in range(X)] for j in range(Y)])

    arr.insert(0, [[['.' for i in range(X)] for j in range(Y)] for k in range(Z)])
    arr.append([[['.' for i in range(X)] for j in range(Y)] for k in range(Z)])

    return arr

def part_2(data, cycles):
    prev, curr = deepcopy(data), deepcopy(data)
    for n in range(cycles):
        prev, curr = expand_arr_v2(prev), expand_arr_v2(curr)
        X, Y, Z, W = len(prev[0][0][0]), len(prev[0][0]), len(prev[0]), len(prev)

        for h in range(W):
            for k in range(Z):
                for j in range(Y):
                    for i in range(X):
                        if change_state_v2(prev, i, j, k, h):
                            if prev[h][k][j][i] == '#':
                                curr[h][k][j][i] = '.'
                            else:
                                curr[h][k][j][i] = '#'
            
        prev = deepcopy(curr)
    
    X, Y, Z, W = len(prev[0][0][0]), len(prev[0][0]), len(prev[0]), len(prev)
    active = 0
    for h in range(W):
        for k in range(Z):
            for j in range(Y):
                for i in range(X):
                    if prev[h][k][j][i] == '#':
                        active += 1
    
    return active



ans_2 = part_2(part_2_data, 6)
print(f'Part 2: {ans_2}')