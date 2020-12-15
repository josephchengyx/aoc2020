data = [9,6,0,10,18,2,1]

def memory_game(data, end):
    t = 1
    prev = data[0]
    memo = dict()
    while t < end:
        if t < len(data):
            curr = data[t]
        else:
            if prev not in memo:
                curr = 0
            else:
                curr = t - memo[prev]
        memo[prev] = t
        prev = curr
        t += 1
    return curr

ans_1 = memory_game(data, 2020)
ans_2 = memory_game(data, 30000000)
print(f'Part 1: {ans_1}')
print(f'Part 2: {ans_2}')