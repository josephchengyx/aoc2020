import csv

with open('day5_input.csv', newline='') as f:
    reader = csv.reader(f)
    data = list()
    for line in reader:
        data.append(line[0])

# print(data[:10])



def decode(strng):
    if len(strng) == 7:
        l, r = 0, 127
    else:
        l, r = 0, 7
    for c in strng:
        if c == 'F' or c == 'L':
            r = (l + r)//2
        else:
            l = (l + r)//2 + 1
        # print(f'{l}, {r}')
    return l

# decode('FBFBBFF')
# decode('RLR')

def part_1(data):
    result = list()
    for line in data:
        row = decode(line[:7])
        col = decode(line[7:])
        seat_id = row * 8 + col
        result.append(seat_id)
    return result



def part_2(data):
    data = sorted(data)
    i = 0
    while i < len(data)-1:
        seat_id, next_id = data[i], data[i+1]
        if seat_id + 2 == next_id:
            return seat_id + 1
        i += 1



seat_ids = part_1(data)
ans_1 = max(seat_ids)
ans_2 = part_2(seat_ids)
print(f'Part 1: {ans_1}')
print(f'Part 2: {ans_2}')
