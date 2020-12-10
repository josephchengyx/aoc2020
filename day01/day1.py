import csv

with open('day1_input.csv', newline='') as f:
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    data = list()
    for line in reader:
        data.append(line[0])

# print(data)

def part_1(data, total):
    for i in range(len(data)):
        x = data[i]
        y = total - x
        if y in data and data.index(y) != i:
            return x, y
    return 0, 0

def part_2(data, total):
    for i in range(len(data)):
        x = data[i]
        sub = total - x
        y, z = part_1(data, sub)
        if y + z == sub and data.index(y) != i and data.index(z) != i:
            return x, y, z
    return 0, 0, 0

a11, a12 = part_1(data, 2020)
a21, a22, a23 = part_2(data, 2020)
ans_1 = a11 * a12
ans_2 = a21 * a22 * a23
print(f'Part 1: {a11}, {a12}, product {ans_1}')
print(f'Part 2: {a21}, {a22}, {a23}, product {ans_2}')
