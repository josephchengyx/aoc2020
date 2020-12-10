import csv

with open('day3_input.csv', newline='') as f:
    reader = csv.reader(f)
    data = list()
    for line in reader:
        data.append(line[0])

# print(data[:10])

def part_1(data, rt, dn):
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

ans_1 = part_1(data, 3, 1)
a21, a22, a23, a24 = part_1(data, 1, 1), part_1(data, 5, 1), part_1(data, 7, 1), part_1(data, 1, 2)
ans_2 = ans_1 * a21 * a22 * a23 * a24
print(f'Part 1: {ans_1}')
print(f'Part 2: {ans_2}')
