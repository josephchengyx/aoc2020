with open('day3_input.txt', newline='') as f:
    reader = f.read().splitlines()
    data = list()
    for line in reader:
        data.append(line)

# print(data[:10])

def count_trees(data, rt, dn):
    trees = 0
    x, y = 0, 0
    m, n = len(data), len(data[0])
    while y < m:
        if data[y][x] == '#':
            trees += 1
        x += rt
        y += dn
        if x >= n:
            x -= n
    return trees

ans_1 = count_trees(data, 3, 1)
a21, a22, a23, a24 = count_trees(data, 1, 1), count_trees(data, 5, 1), count_trees(data, 7, 1), count_trees(data, 1, 2)
ans_2 = ans_1 * a21 * a22 * a23 * a24
print(f'Part 1: {ans_1}')
print(f'Part 2: {ans_2}')