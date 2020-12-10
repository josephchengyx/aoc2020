import csv

with open('day9_input.csv', newline='') as f:
    reader = csv.reader(f)
    data = list()
    for line in reader:
        data.append(int(line[0]))

# print(data[:10])



def check_pair(lst, num):
    for i in range(len(lst)):
        x = lst[i]
        y = num - x
        if y in lst and lst.index(y) != i:
            return True
    return False

def part_1(data):
    preamble = data[:25]
    for i in range(25, len(data)):
        n = data[i]
        if not check_pair(preamble, n):
            return n
        else:
            preamble.pop(0)
            preamble.append(n)



def part_2_alt(data, target):
    m, n = 0, 2
    total = sum(data[m:n])
    while n <= len(data):
        if total == target:
            return data[m:n]
        elif total < target:
            total += data[n]
            n += 1
        else:
            total -= data[m]
            m += 1



ans_1 = part_1(data)
seq = part_2_alt(data, ans_1)
ans_2 = min(seq) + max(seq)
print(f'Part 1: {ans_1}')
# print(seq)
print(f'Part 2: {ans_2}')
