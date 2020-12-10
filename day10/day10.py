import csv

with open('day10_input.csv', newline='') as f:
    reader = csv.reader(f)
    data = list()
    for line in reader:
        data.append(int(line[0]))
    data = sorted(data)

# print(data)



def part_1(data):
    diff = {1: 0, 2: 0, 3: 1}
    for i in range(len(data)):
        if i == 0:
            d = data[i]
        else:
            d = data[i] - data[i-1]
        if d in diff:
            diff[d] += 1
    return diff



def diff_arr(data):
    res = [data[0]]
    for i in range(1, len(data)):
        d = data[i] - data[i-1]
        res.append(d)
    return tuple(res)

part_2_memo = dict()
def part_2(data):
    if data in part_2_memo:
        return part_2_memo[data]
    else:
        if len(data) < 2:
            res = 1
        else:
            if data[0] + data[1] < 4:
                data2 = (data[0]+data[1],) + data[2:]
                res = part_2(data[1:]) + part_2(data2)
            else:
                res = part_2(data[1:])
        part_2_memo[data] = res
        return res



diff_dict = part_1(data)
# print(diff_dict)
ans_1 = diff_dict[1] * diff_dict[3]
print(f'Part 1: {ans_1}')

diff_data = diff_arr(data)
# print(diff_data)
ans_2 = part_2(diff_data)
print(f'Part 2: {ans_2}')