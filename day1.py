import csv

with open('day1_input.csv', newline='') as f:
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    data = list()
    for line in reader:
        data.append(line[0])

# print(data)

def part_1(data, total):
    for n in data:
        x = total - n
        if x in data and x != n:
            return n, x
    return 0, 0

def part_2(data, total):
    for n in data:
        m = total - n
        x, y = part_1(data, m)
        if x + y == m and n != x and n!= y:
            return n, x, y
    return 0, 0, 0

a11, a12 = part_1(data, 2020)
a21, a22, a23 = part_2(data, 2020)
print(f'Part 1: {a11}, {a12}, product {a11*a12}')
print(f'Part 2: {a21}, {a22}, {a23}, product {a21*a22*a23}')