data = 247819356

def parse(data):
    return tuple(map(int, list(str(data))))

data = parse(data)
# print(data)



def parse_v2(data):
    N = len(data)
    res = [0] * N
    for i in range(N):
        cur = data[i]
        if i == N-1:
            nxt = data[0]
        else:
            nxt = data[i+1]
        res[cur-1] = nxt
    return res, data[0]

def unparse(data):
    N, n = len(data), data.index(1)+1
    res = list()
    for i in range(N):
        n = data[n-1]
        res.append(n)
    return ''.join(map(str, res))

def move_cups(data, ini, moves):
    minn, maxx = min(data), max(data)
    curr = ini
    for move in range(moves):
        up1 = data[curr-1]
        up2 = data[up1-1]
        up3 = data[up2-1]
        curr_nxt = data[up3-1]
        dest = curr - 1
        while dest in (up1, up2, up3) or dest < minn:
            dest -= 1
            if dest < minn:
                dest = maxx
        dest_nxt = data[dest-1]
        data[dest-1] = up1
        data[up3-1] = dest_nxt
        data[curr-1] = curr_nxt
        curr = curr_nxt
    return data



def part_1(data):
    data, ini = parse_v2(data)
    res = move_cups(data, ini, 100)
    return unparse(res)[1:]

def part_2(data):
    data, ini = parse_v2(data + tuple(range(10, 1_000_001)))
    res = move_cups(data, ini, 10_000_000)
    r1 = res[0]
    r2 = res[r1-1]
    return r1 * r2



ans_1 = part_1(data)
ans_2 = part_2(data)
print(f'Part 1: {ans_1}')
print(f'Part 2: {ans_2}')