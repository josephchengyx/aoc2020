import csv
from time import sleep

with open('day8_input.csv', newline='') as f:
    reader = csv.reader(f)
    data = list()
    for line in reader:
        data.append(line[0])

# print(data[:10])

with open('day8_fixed.csv', newline='') as f:
    reader = csv.reader(f)
    fixed_data = list()
    for line in reader:
        fixed_data.append(line[0])

def parse(data):
    for i in range(len(data)):
        line = data[i]
        cmd = line[:3]
        sgn = line[4]
        num = int(line[5:])
        if sgn == '-':
            num = -num
        data[i] = (cmd, num)
    return data

data = parse(data)
fixed_data = parse(fixed_data)
# print(data[:10])



def part_1(data):
    acc = 0
    i = 0
    seen = list()
    while i not in seen and i < len(data):
        seen.append(i)
        line = data[i]
        cmd, num = line[0], line[1]
        if cmd == 'acc':
            acc += num
            i += 1
        elif cmd == 'jmp':
            i += num
        else:
            i += 1
    return acc
    


def trace(data):
    i = 0
    seen = list()
    while i not in seen and i < len(data):
        seen.append(i)
        line = data[i]
        cmd, num = line[0], line[1]
        print(f'{i+1}. {line}')
        if cmd == 'jmp':
            i += num
        else:
            i += 1
        sleep(0.1)
    if i >= len(data):
        print('Program terminates\n')
    else:
        print('Program loops\n')

def check_loop(data, idx):
    i = 0
    seen = list()
    while i not in seen and i < len(data):
        seen.append(i)
        line = data[i]
        cmd, num = line[0], line[1]
        if i == idx:
            if cmd == 'jmp':
                i += 1
            else:
                i += num
        elif cmd == 'jmp':
            i += num
        else:
            i += 1
    if i in seen:
        return True
    else:
        return False

def fix(data):
    chk_list = list(filter(lambda x: data[x][0] == 'nop' or data[x][0] == 'jmp', range(len(data))))
    for idx in chk_list:
        if not check_loop(data, idx):
            return idx + 1

# trace(data)
idx = fix(data)
print(f'Change instruction at line {idx}')
# trace(fixed_data)



ans_1 = part_1(data)
ans_2 = part_1(fixed_data)
print(f'Part 1: {ans_1}')
print(f'Part 2: {ans_2}')