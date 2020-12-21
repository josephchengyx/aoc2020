from math import prod

with open('day20_input.txt', newline='') as f:
    reader = f.read().splitlines()
    data, temp = list(), list()
    for line in reader:
        if line == '':
            data.append(temp)
            temp = list()
        else:
            temp.append(line)
    data.append(temp)

# print(data[:4])
# print(len(data))

def parse_data(data):
    res = dict()
    for line in data:
        ID = int(line[0][5:-1])
        tile = line[1:]
        res[ID] = tile
    return res

tile_dic = parse_data(data)
# print(tile_dic[1409])



def u_edge(tile):
    return tile[0]

def d_edge(tile):
    return tile[-1]

def l_edge(tile):
    res = ''
    for line in tile:
        res += line[0]
    return res

def r_edge(tile):
    res = ''
    for line in tile:
        res += line[-1]
    return res

def match_tiles(data):
    dirn = {0: 'u', 1: 'd', 2: 'l', 3: 'r'}
    res = {ID: [0, 0, 0, 0] for ID in data}
    for ID, tile in data.items():
        edges = [u_edge(tile), d_edge(tile), l_edge(tile), r_edge(tile)]
        for i in range(4):
            if res[ID][i] != 0:
                pass
            edge = edges[i]
            match = False
            for ID2, tile2 in data.items():
                if ID == ID2:
                    continue
                if edge == u_edge(tile2) or edge == u_edge(tile2)[::-1]:
                    res[ID][i] = (ID2, 'u')
                    res[ID2][0] = (ID, dirn[i])
                    match = True
                    break
                elif edge == d_edge(tile2) or edge == d_edge(tile2)[::-1]:
                    res[ID][i] = (ID2, 'd')
                    res[ID2][1] = (ID, dirn[i])
                    match = True
                    break
                elif edge == l_edge(tile2) or edge == l_edge(tile2)[::-1]:
                    res[ID][i] = (ID2, 'l')
                    res[ID2][2] = (ID, dirn[i])
                    match = True
                    break
                elif edge == r_edge(tile2) or edge == r_edge(tile2)[::-1]:
                    res[ID][i] = (ID2, 'r')
                    res[ID2][3] = (ID, dirn[i])
                    match = True
                    break
            if not match:
                res[ID][i] = (-1, '')
    return res

def part_1(img):
    corners = list()
    for ID, edges in img.items():
        n = 0
        for i in range(4):
            edge = edges[i]
            if edge[0] == -1:
                n += 1
        if n >= 2:
            corners.append(ID)
    return corners



def ud_flip(tile):
    return tile[::-1]

def lr_flip(tile):
    res = list()
    for line in tile:
        res.append(line[::-1])
    return res

def cw_rotate(tile):
    res = list()
    for j in range(len(tile[0])):
        row = ''
        for i in range(len(tile)):
            row += tile[i][j]
        res.append(row[::-1])
    return res

def cc_rotate(tile):
    res = list()
    for j in range(len(tile[0])):
        row = ''
        for i in range(len(tile)):
            row += tile[i][j]
        res.append(row)
    return res[::-1]

def rotate_180(tile):
    return lr_flip(ud_flip(tile))

def join_tiles(tile1, tile2):
    if not tile1:
        return tile2
    res = list()
    for i in range(len(tile1)):
        res.append(tile1[i] + tile2[i])
    return res

def remove_borders(tile):
    res = list()
    for i in range(1, len(tile)-1):
        row = tile[i]
        res.append(row[1:-1])
    return res

def assemble_img(instr, data, ini):
    img = list()
    d_curr = ini
    prev_d_edge = ''

    while d_curr[0] != -1:
        i_ID, i_ori = d_curr[0], d_curr[1]
        i_tile = data[i_ID]
        flip = False

        if i_ori == 'd':
            i_tile = rotate_180(i_tile)
            r_nxt, d_nxt = 2, 0
        elif i_ori == 'l':
            i_tile = cw_rotate(i_tile)
            r_nxt, d_nxt = 0, 3
        elif i_ori == 'r':
            i_tile = cc_rotate(i_tile)
            r_nxt, d_nxt = 1, 2
        else:
            r_nxt, d_nxt = 3, 1

        if u_edge(i_tile) == prev_d_edge[::-1]:
            i_tile = lr_flip(i_tile)
            flip = True

        if flip:
            if i_ori == 'd':
                r_nxt = 3
            elif i_ori == 'l':
                r_nxt = 1
            elif i_ori == 'r':
                r_nxt = 0
            else:
                r_nxt = 2

        prev_r_edge, prev_d_edge = r_edge(i_tile), d_edge(i_tile) 
        row = remove_borders(i_tile)    
        r_curr, d_curr = instr[i_ID][r_nxt], instr[i_ID][d_nxt]

        while r_curr[0] != -1:
            ID, ori = r_curr[0], r_curr[1]
            tile = data[ID]

            if ori == 'u':
                tile = cc_rotate(tile)
                nxt = 1
            elif ori == 'd':
                tile = cw_rotate(tile)
                nxt = 0
            elif ori == 'r':
                tile = rotate_180(tile)
                nxt = 2
            else:
                nxt = 3

            if l_edge(tile) == prev_r_edge[::-1]:
                tile = ud_flip(tile)

            prev_r_edge = r_edge(tile)
            row = join_tiles(row, remove_borders(tile))
            r_curr = instr[ID][nxt]
        
        img.extend(row)
    
    return img



def convolution(data):
    krnl = ['                  # ', '#    ##    ##    ###', ' #  #  #  #  #  #   ']
    m, d = len(krnl), len(krnl[0])
    filtr = list()
    for i in range(m):
        for j in range(d):
            if krnl[i][j] == '#':
                filtr.append((i, j))
    n = len(filtr)

    tot = 0
    for y in range(len(data) - m + 1):
        for x in range(len(data[0]) - d + 1):
            convl = [row[x:x+d] for row in data[y:y+m]]
            match = True
            for i, j in filtr:
                if convl[i][j] != '#':
                    match = False
                    break
            if match:
                tot += n
    
    return tot

def part_2(img):
    chk_lst = [img, cc_rotate(img), cw_rotate(img), rotate_180(img), ud_flip(img), cc_rotate(ud_flip(img)), cw_rotate(ud_flip(img)), lr_flip(img)]
    for item in chk_lst:
        res = convolution(item)
        if res > 0:
            return sum(map(lambda row: row.count('#'), img)) - res
    return 0



def print_img(img):
    for row in img:
        print(row)

img_dic = match_tiles(tile_dic)
corners = part_1(img_dic)
ans_1 = prod(corners)

start_tile = (corners[0], 'u')
img = assemble_img(img_dic, tile_dic, start_tile)
# print_img(img)
ans_2 = part_2(img)

print(f'Part 1: {ans_1}')
print(f'Part 2: {ans_2}')