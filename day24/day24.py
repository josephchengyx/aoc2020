from copy import deepcopy

with open('day24_input.txt', newline='') as f:
    reader = f.read().splitlines()
    data = list()
    for line in reader:
        data.append(line)

# print(data[:10])

def print_arr(arr):
    for row in arr:
        print(row)



def flip_tiles(data):
    hexgrid = dict()
    for line in data:
        x, y = 0, 0
        i = 0

        while i < len(line):
            char = line[i]
            if char == 's' or char == 'n':
                char = line[i:i+2]
                i += 1
            i += 1

            if char == 'e':
                x += 2
            elif char == 'se':
                x += 1
                y += 1
            elif char == 'sw':
                x -= 1
                y += 1
            elif char == 'w':
                x -= 2
            elif char == 'nw':
                x -= 1
                y -= 1
            elif char == 'ne':
                x += 1
                y -= 1
            
        if (x, y) not in hexgrid or hexgrid[(x, y)] == 'w':
            hexgrid[(x, y)] = 'b'
        else:
            hexgrid[(x, y)] = 'w'
    
    return hexgrid

def part_1(hexgrid):
    black_tiles = list()
    for tile, color in hexgrid.items():
        if color == 'b':
            black_tiles.append(tile)
    return len(black_tiles)



def expand_arr(arr):
    X = len(arr[0]) + 4
    for row in arr:
        if row[0] == ' ':
            row.insert(0, 'w')
            row.insert(0, ' ')
            row.append('w')
            row.append(' ')
        else:
            row.insert(0, ' ')
            row.insert(0, 'w')
            row.append(' ')
            row.append('w')
    
    if arr[0][0] == ' ':
        arr.insert(0, ['w' if i % 2 == 0 else ' ' for i in range(X)])
        arr.append(['w' if i % 2 == 0 else ' ' for i in range(X)])
    else:
        arr.insert(0, ['w' if i % 2 == 1 else ' ' for i in range(X)])
        arr.append(['w' if i % 2 == 1 else ' ' for i in range(X)])
    
    return arr

def check_border(arr):
    Y = len(arr)
    res = arr[0] + arr[-1]
    for j in range(1, Y-1):
        res.extend(arr[j][:2])
        res.extend(arr[j][-2:])
    for char in res:
        if char == 'b':
            return True
    return False

def construct_hexarr(hexgrid):
    x_coords = [x for x, y in hexgrid.keys()]
    y_coords = [y for x, y in hexgrid.keys()]
    X1, X2 = min(x_coords), max(x_coords)
    Y1, Y2 = min(y_coords), max(y_coords)
    X, Y = X2 - X1 + 1, Y2 - Y1 + 1

    hexarr = [['w' if (i + j) % 2 == 1 else ' ' for i in range(X)] for j in range(Y)]
    for coord, val in hexgrid.items():
        x, y = coord
        x -= X1
        y -= Y1
        hexarr[y][x] = val
    
    hexarr = expand_arr(hexarr)
    return hexarr

def part_2(hexgrid, iters):
    ref = construct_hexarr(hexgrid)
    for itr in range(iters):
        X, Y = len(ref[0]), len(ref)
        nxt = deepcopy(ref)

        for j in range(Y):
            for i in range(X):
                tile = ref[j][i]
                if tile == ' ':
                    continue
                adj = [(i+2, j), (i+1, j+1), (i-1, j+1), (i-2, j), (i-1, j-1), (i+1, j-1)]
                count = 0

                for coord in adj:
                    x, y = coord
                    try:
                        col = ref[y][x]
                    except IndexError:
                        col = 'w'
                    if col == 'b':
                        count += 1
                
                if tile == 'b' and (count == 0 or count > 2):
                    nxt[j][i] = 'w'
                elif tile == 'w' and count == 2:
                    nxt[j][i] = 'b'
                
        if check_border(nxt):
            nxt = expand_arr(nxt)
        ref = nxt
    
    res = 0
    for j in range(len(ref)):
        for i in range(len(ref[0])):
            if ref[j][i] == 'b':
                res += 1
    return res



ini_config = flip_tiles(data)
ans_1 = part_1(ini_config)
ans_2 = part_2(ini_config, 100)
print(f'Part 1: {ans_1}')
print(f'Part 2: {ans_2}')