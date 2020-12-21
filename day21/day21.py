with open('day21_input.txt', newline='') as f:
    reader = f.read().splitlines()
    data = list()
    for line in reader:
        data.append(line)

# print(data[:3])

def parse(data):
    ings, alrs = list(), list()
    for line in data:
        idx = line.index('(')
        ing = line[:idx-1].split(' ')
        alr = line[idx+10:-1].split(', ')
        ings.append(ing)
        alrs.append(alr)
    return ings, alrs

ings, alrs = parse(data)
combined = list(zip(ings, alrs))
# print(ings[:3])
# print(alrs[:3])
# print(combined[:3])



def possible_alrs(alrs, data):
    poss = dict()
    alrs_lst = list({item for lst in alrs for item in lst})
    for alr in alrs_lst:
        foods = filter(lambda row: alr in row[1], data)
        temp = list()
        for item in foods:
            temp.append(set(item[0]))
        poss[alr] = set.intersection(*temp)
    return poss

def part_1(ings, poss):
    ings_lst = [item for lst in ings for item in lst]
    alrs_lst = set().union(*poss.values())
    i = 0
    while i < len(ings_lst):
        item = ings_lst[i]
        if item in alrs_lst:
            ings_lst.remove(item)
        else:
            i += 1
    return len(ings_lst)



def confirmed_alrs(poss):
    cfmd = dict()
    while len(cfmd) < len(poss):
        for key, val in poss.items():
            if len(val) == 1:
                ing = val.pop()
                cfmd[key] = ing
                break
        for key, val in poss.items():
            if ing in val:
                val.remove(ing)
    return cfmd

def part_2(cfmd):
    res = [(key, val) for key, val in cfmd.items()]
    res = sorted(res, key=lambda tup: tup[0])
    res = [tup[1] for tup in res]
    return ','.join(res)



poss = possible_alrs(alrs, combined)
# print(poss)
ans_1 = part_1(ings, poss)

cfmd = confirmed_alrs(poss)
# print(cfmd)
ans_2 = part_2(cfmd)

print(f'Part 1: {ans_1}')
print(f'Part 2: {ans_2}')