import csv

with open('day4_input.csv', newline='') as f:
    reader = csv.reader(f)
    data = list()
    temp_list = list()
    for line in reader:
        if line:
            line = line[0].split(' ')
            for word in line:
                temp_list.append(word)
        else:
            data.append(temp_list)
            temp_list = list()
    data.append(temp_list)

# print(data[:10])



def part_1(data):
    count = 0
    for line in data:
        valid = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
        for entry in line:
            field = entry[:3]
            if field in valid:
                valid.remove(field)
        if not valid:
            count += 1
    return count



def yr_check(x, field):
    if x.isnumeric():
        x = int(x)
        if (field == 'byr' and x >= 1920 and x <= 2002) or (field == 'iyr' and x >= 2010 and x <= 2020) or (field == 'eyr' and x >= 2020 and x <= 2030):
            return True
    return False

def hgt_check(x):
    num, unit = x[:-2], x[-2:]
    if num.isnumeric():
        num = int(num)
        if (unit == 'cm' and num >= 150 and num <= 193) or (unit == 'in' and num >= 59 and num <= 76):
            return True
    return False

def hcl_check(x):
    if x[0] == '#':
        for c in x[1:]:
            if c not in '0123456789abcdef':
                return False
        return True
    return False

def ecl_check(x):
    if x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return True
    return False

def pid_check(x):
    if len(x) == 9 and x.isnumeric():
        return True
    return False

def validation(field, x):
    if field in ['byr', 'iyr', 'eyr']:
        return yr_check(x, field)
    elif field == 'hgt':
        return hgt_check(x)
    elif field == 'hcl':
        return hcl_check(x)
    elif field == 'ecl':
        return ecl_check(x)
    elif field == 'pid':
        return pid_check(x)
    else:
        return False



def part_2(data):
    count = 0
    for line in data:
        valid = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
        for entry in line:
            field, x = entry[:3], entry[4:]
            if field in valid and validation(field, x):
                valid.remove(field)
        if not valid:
            count += 1
    return count



ans_1 = part_1(data)
ans_2 = part_2(data)
print(f'Part 1: {ans_1}')
print(f'Part 2: {ans_2}')
