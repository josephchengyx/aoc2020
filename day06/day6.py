with open('day6_input.txt', newline='') as f:
    reader = f.read().splitlines()
    data = list()
    temp_list = list()
    for line in reader:
        if line:
            line = line.split(' ')
            for word in line:
                temp_list.append(word)
        else:
            data.append(temp_list)
            temp_list = list()
    data.append(temp_list)

# print(data[:10])

def part_1(data):
    total = 0
    for line in data:
        pool = set()
        for entry in line:
            for c in entry:
                pool.add(c)
        total += len(pool)
    return total

def part_2(data):
    total = 0
    for line in data:
        for i in range(len(line)):
            line[i] = set(line[i])
        line = set.intersection(*line)
        total += len(line)
    return total

ans_1 = part_1(data)
ans_2 = part_2(data)
print(f'Part 1: {ans_1}')
print(f'Part 2: {ans_2}')