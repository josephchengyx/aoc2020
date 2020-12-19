with open('day19_input.txt', newline='') as f:
    reader = f.read().splitlines()
    data = list()
    for line in reader:
        data.append(line)

def parse_rules_list(data):
    res = dict()
    for line in data:
        i = line.index(':')
        num = int(line[:i])
        val = line[i+2:]
        res[num] = val
    return res

rules = parse_rules_list(data[:128])
msgs = data[129:]



def combine(args):
    res = list()
    if len(args) == 1:
        return args[0]
    if len(args) > 2:
        arg1, arg2 = args[0], combine(args[1:])
    else:
        arg1, arg2 = args[0], args[1]
    for x in arg1:
        for y in arg2:
            res.append(x + y)
    return res

rule_memo = dict()
def read_rule(rules, n):
    if n in rule_memo:
        return rule_memo[n]
    else:
        rule = rules[n]
        if '"' in rule:
            res = [rule[1:-1]]
        elif '|' not in rule:
            r1 = map(int, rule.split(' '))
            r1 = list(map(lambda r: read_rule(rules, r), r1))
            res = combine(r1)
        else:
            i = rule.index('|')
            r1, r2 = rule[:i-1], rule[i+2:]
            r1, r2 = map(int, r1.split(' ')), map(int, r2.split(' '))
            r1, r2 = list(map(lambda r: read_rule(rules, r), r1)), list(map(lambda r: read_rule(rules, r), r2))
            res = combine(r1) + combine(r2)
        rule_memo[n] = res
        return res

def binary_search(arr, x):
    l, r = 0, len(arr)-1
    while l <= r:
        i = (l + r)//2
        if arr[i] == x:
            return True
        elif arr[i] < x:
            l = i + 1
        else:
            r = i - 1
    return False

def part_1(rule, msgs):
    rule = sorted(rule)
    count = 0
    for msg in msgs:
        if binary_search(rule, msg):
            count += 1
    return count



def new_rules(rule31, rule42, msg):
    n31, n42 = 0, 0
    bool31, bool42 = True, True

    while msg and bool31:
        bool31 = False
        for r in rule31:
            if msg.endswith(r):
                n31 += 1
                msg = msg[:-len(r)]
                bool31 = True
    
    if n31 < 1:
        return False
    
    while msg and bool42:
        bool42 = False
        for r in rule42:
            if msg.endswith(r):
                n42 += 1
                msg = msg[:-len(r)]
                bool42 = True

    if not msg and n42 >= n31+1:
        return True
    else:
        return False

def part_2(rule0, rule31, rule42, msgs):
    rule0 = sorted(rule0)
    count = 0
    for msg in msgs:
        if binary_search(rule0, msg) or new_rules(rule31, rule42, msg):
            count += 1
    return count



rule_zero = read_rule(rules, 0)
ans_1 = part_1(rule_zero, msgs)

rule_31 = read_rule(rules, 31)
rule_42 = read_rule(rules, 42)
ans_2 = part_2(rule_zero, rule_31, rule_42, msgs)

print(f'Part 1: {ans_1}')
print(f'Part 2: {ans_2}')