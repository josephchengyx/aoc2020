with open('day14_input.txt', newline='') as f:
    reader = f.read().splitlines()
    data = list()
    for line in reader:
        data.append(line)

# print(data[:10])

def parse(data):
    for i in range(len(data)):
        line = data[i]
        if line[:4] == 'mask':
            idx = line.index('=')
            val = line[idx+2:]
            data[i] = ('mask', val)
        else:
            idx = line.index(']')
            loc, val = int(line[4:idx]), int(line[idx+4:])
            data[i] = (loc, val)
    return data

data = parse(data)
# print(data[:10])



def part_1(data):
    mem = dict()
    for line in data:
        if line[0] == 'mask':
            mask = line[1]
        else:
            loc, val = line[0], line[1]
            val = format(val, '036b')
            inp = ''
            for i in range(36):
                if mask[i] == 'X':
                    inp += val[i]
                else:
                    inp += mask[i]
            inp = int(inp, 2)
            mem[loc] = inp
    return sum(mem.values())



def part_2(data):
    mem = dict()
    for line in data:
        if line[0] == 'mask':
            mask = line[1]
            X = mask.count('X')
            flt = list()
            for i in range(2**X):
                flt.append(format(i, f'0{X}b'))
        else:
            loc, val = line[0], line[1]
            loc = format(loc, '036b')
            for i in range(len(flt)):
                temp = flt[i]
                dest = ''
                for j in range(36):
                    if mask[j] == '0':
                        dest += loc[j]
                    elif mask[j] == 'X':
                        dest += temp[0]
                        temp = temp[1:]
                    else:
                        dest += mask[j]
                dest = int(dest, 2)
                mem[dest] = val
    return sum(mem.values())



ans_1 = part_1(data)
ans_2 = part_2(data)
print(f'Part 1: {ans_1}')
print(f'Part 2: {ans_2}')