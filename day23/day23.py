data = 247819356

def parse(data):
    return list(map(int, list(str(data))))

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
    def nxt(i, n):
        if n < 2:
            return data[i-1]
        else:
            return data[nxt(i, n-1)-1]
    minn, maxx = min(data), max(data)
    curr = ini
    for move in range(moves):
        up = (nxt(curr, 1), nxt(curr, 2), nxt(curr, 3))
        curr_nxt = nxt(curr, 4)
        dest = curr - 1
        while dest in up or dest < minn:
            dest -= 1
            if dest < minn:
                dest = maxx
        dest_nxt = nxt(dest, 1)
        data[dest-1] = up[0]
        data[up[-1]-1] = dest_nxt
        data[curr-1] = curr_nxt
        curr = curr_nxt
    return data



part_1_data, ini = parse_v2(data)
part_1_res = move_cups(part_1_data, ini, 100)
ans_1 = unparse(part_1_res)[1:]

part_2_data, ini = parse_v2(data + list(range(10, 1_000_001)))
part_2_res = move_cups(part_2_data, ini, 10_000_000)
a21 = part_2_res[0]
a22 = part_2_res[a21-1]
ans_2 = a21 * a22

print(f'Part 1: {ans_1}')
print(f'Part 2: {ans_2}')