from math import prod

with open('day16_input.txt', newline='') as f:
    reader = f.read().splitlines()
    data = list()
    for line in reader:
        data.append(line)

# print(data[:50])

def parse_fields(data):
    res = dict()
    for line in data:
        idx1 = line.index(':')
        name = line[:idx1]
        nums = line[idx1+2:]
        idx2 = nums.index('or')
        lw = nums[:idx2-1]
        up = nums[idx2+3:]
        idx3 = lw.index('-')
        idx4 = up.index('-')
        lw1, lw2 = int(lw[:idx3]), int(lw[idx3+1:])
        up1, up2 = int(up[:idx4]), int(up[idx4+1:])
        res[name] = (lw1, lw2, up1, up2)
    return res

fields = parse_fields(data[:20])
# print(fields)

my_ticket = [int(n) for n in data[22].split(',')]
# print(my_ticket)

nearby_tix = data[25:]
for i in range(len(nearby_tix)):
    nearby_tix[i] = [int(n) for n in nearby_tix[i].split(',')]
# print(nearby_tix[:10])



def invalid_tix(fields, val):
    for field in fields.values():
        lw1, lw2, up1, up2 = field[0], field[1], field[2], field[3]
        if (val >= lw1 and val <= lw2) or (val >= up1 and val <= up2):
            return False
    return True

def part_1(tickets, fields):
    inval_vals = list()
    for tix in tickets:
        for val in tix:
            if invalid_tix(fields, val):
                inval_vals.append(val)
    return sum(inval_vals)



def discard_inval(tickets, fields):
    remaining = list()
    for tix in tickets:
        valid = True
        for val in tix:
            if invalid_tix(fields, val):
                valid = False
                break
        if valid:
            remaining.append(tix)
    return remaining

def match_fields(tickets, fields):
    def valid(fields, name, val):
        tup = fields[name]
        lw1, lw2, up1, up2 = tup[0], tup[1], tup[2], tup[3]
        return True if (val >= lw1 and val <= lw2) or (val >= up1 and val <= up2) else False
    
    N = len(fields)
    chk_lst = list()
    for i in range(N):
        col = [key for key in fields.keys()]
        chk_lst.append(col)
    
    for i in range(N):
        lst = chk_lst[i]
        j = 0
        while j < len(lst):
            name = lst[j]
            inval = False
            for tix in tickets:
                val = tix[i]
                if not valid(fields, name, val):
                    inval = True
                    break
            if inval:
                lst.pop(j)
            else:
                j += 1
    
    chk_lst = list(zip(range(N), chk_lst))
    chk_lst.sort(key=lambda tup: len(tup[1]))
    remove_lst = list()

    for tup in chk_lst:
        lst = tup[1]
        for name in remove_lst:
            lst.remove(name)
        remove_lst.append(lst[0])

    chk_lst.sort(key=lambda tup: tup[0])
    chk_lst = tuple(tup[1][0] for tup in chk_lst)

    return chk_lst

def part_2(tix, positions):
    res = list()
    for i in range(len(positions)):
        if 'departure' in positions[i]:
            res.append(tix[i])
    return prod(res)

valid_tix = discard_inval(nearby_tix, fields)
valid_tix.insert(0, my_ticket)
# print(valid_tix[:10])

positions = match_fields(valid_tix, fields)
# print(positions)



ans_1 = part_1(nearby_tix, fields)
ans_2 = part_2(my_ticket, positions)
print(f'Part 1: {ans_1}')
print(f'Part 2: {ans_2}')