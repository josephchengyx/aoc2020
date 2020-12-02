import csv

def parse(strng):
    ln = strng.split()
    d = ln[0].index('-')
    lw = int(ln[0][:d])
    up = int(ln[0][d+1:])
    char = ln[1][0]
    return (lw, up, char, ln[2])

with open('day2_input.csv', newline='') as f:
    reader = csv.reader(f)
    data = list()
    for line in reader:
        data.append(parse(line[0]))

# print(data[:10])

def part_1(data):
    total = 0
    for line in data:
        lw, up, char, pword = line
        count = pword.count(char)
        if count >= lw and count <= up:
            total += 1
    return total

def part_2(data):
    total = 0
    for line in data:
        lw, up, char, pword = line
        lchar, uchar = pword[lw-1], pword[up-1]
        if (lchar == char and uchar != char) or (lchar != char and uchar == char):
            total += 1
    return total

ans_1 = part_1(data)
ans_2 = part_2(data)
print(f'Part 1: {ans_1}')
print(f'Part 2: {ans_2}')