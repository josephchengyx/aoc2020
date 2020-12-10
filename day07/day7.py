import csv

with open('day7_input.csv', newline='') as f:
    reader = csv.reader(f)
    data = list()
    for line in reader:
        data.append(line)

# print(data[:10])

def parse(data):
    result = dict()
    for line in data:
        value = list()
        temp = line[0].split('contain')
        x = temp[0].index('bag')
        key = temp[0][:x-1]
        x = temp[1].index('bag')
        try:
            n = int(temp[1][1])
        except ValueError:
            n = 0
        color = temp[1][3:x-1]
        value.extend(n*[color])
        for i in range(1, len(line)):
            x = line[i].index('bag')
            n = int(line[i][1])
            color = line[i][3:x-1]
            value.extend(n*[color])
        result[key] = value
    return result

data_dic = parse(data)
# print(data_dic)



def part_1(data, ini):
    result = [ini]
    i = 0
    while i < len(result):
        color = result[i]
        for key, value in data.items():
            if color in value and key not in result:
                result.append(key)
        i += 1
    result.remove(ini)
    return len(result)



def part_2(data, ini):
    count = 0
    for bag in data[ini]:
        count += 1 + part_2(data, bag)
    return count



ans_1 = part_1(data_dic, 'shiny gold')
ans_2 = part_2(data_dic, 'shiny gold')
print(f'Part 1: {ans_1}')
print(f'Part 2: {ans_2}')
