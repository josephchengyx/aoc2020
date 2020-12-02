import csv

with open('day1_input.csv', newline='') as f:
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    data = list()
    for line in reader:
        data.append(line[0])

# print(data)

def part_1(data):
    for n in data:
        x = 2020 - n
        if x in data:
            return n * x

def part_2(data):
    for n in data:
        m = 2020 - n
        for x in data:
            y = m - x
            if y in data:
                return n * x * y

ans_1 = part_1(data)
ans_2 = part_2(data)
print(f'Part 1: {ans_1}')
print(f'Part 2: {ans_2}')