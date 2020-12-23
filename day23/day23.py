'''
Thanks once again to @chuahou for various further runtime optimizations
'''

data = 247819356

def parse(data):
    return tuple(map(int, list(str(data))))

data = parse(data)
# print(data)



def parse_v2(data):
    N = len(data)
    res = [0] * (N+1)
    for i in range(1, N+1):
        cur = data[i-1]
        if i == N:
            nxt = data[0]
        else:
            nxt = data[i]
        res[cur] = nxt
    return res, data[0]

def unparse(data):
    N, n = len(data), data.index(1)
    res = list()
    for i in range(1, N):
        n = data[n]
        res.append(n)
    return ''.join(map(str, res))

def move_cups(data, ini, maxx, moves):
    curr = ini
    for move in range(moves):
        up1 = data[curr]
        up2 = data[up1]
        up3 = data[up2]
        curr_nxt = data[up3]
        dest = curr - 1
        while dest in (up1, up2, up3) or dest < 1:
            dest -= 1
            if dest < 1:
                dest = maxx
        dest_nxt = data[dest]
        data[dest] = up1
        data[up3] = dest_nxt
        data[curr] = curr_nxt
        curr = curr_nxt
    return data



def part_1(data):
    data, ini = parse_v2(data)
    res = move_cups(data, ini, max(data), 100)
    return unparse(res)[1:]

def part_2(data):
    data, ini = parse_v2(data + tuple(range(10, 1_000_001)))
    res = move_cups(data, ini, 1_000_000, 10_000_000)
    r1 = res[1]
    r2 = res[r1]
    return r1 * r2



ans_1 = part_1(data)
ans_2 = part_2(data)
print(f'Part 1: {ans_1}')
print(f'Part 2: {ans_2}')