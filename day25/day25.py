'''
Thanks to Google for the implementation of the baby-step-giant-step algorithm
'''
from math import ceil, sqrt

with open('day25_input.txt', newline='') as f:
    reader = f.read().splitlines()
    data = list()
    for line in reader:
        data.append(int(line))
    data = tuple(data)

# print(data)

# Baby-step-giant-step algorithm
def bsgs(num, g, p):
    m = ceil(sqrt(p-1))

    memo = dict()
    for j in range(m):
        a = pow(g, j, p)
        memo[a] = j
    
    ainv_m = pow(g, m * (p - 2), p)

    for i in range(m):
        y = (num * pow(ainv_m, i, p)) % p
        if y in memo:
            return i * m + memo[y]

    return None

def part_1(data):
    card, door = data
    door_key = bsgs(door, 7, 20201227)
    return pow(card, door_key, 20201227)

ans_1 = part_1(data)
print(f'Part 1: {ans_1}')