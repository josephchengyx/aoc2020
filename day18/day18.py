with open('day18_input.txt', newline='') as f:
    reader = f.read().splitlines()
    data = list()
    for line in reader:
        data.append(line)

# print(data[:10])



def matching_bracket(strng, idx):
    stack = [strng[idx]]
    while idx < len(strng):
        idx += 1
        char = strng[idx]
        if char == '(':
            stack.append(char)
        elif char == ')':
            stack.pop()
        if not stack:
            return idx
    return -1



def part_1(expr):
    res, op = 0, ''
    i = 0
    while i < len(expr):
        char = expr[i]
        if char == '(':
            j = matching_bracket(expr, i)
            char = part_1(expr[i+1:j])
            i = j
        elif char.isnumeric():
            char = int(char)
        elif char == '+' or char == '*':
            op = char
        if isinstance(char, int):
            if not op:
                res = char
            elif op == '+':
                res += char
            elif op == '*':
                res *= char
        i += 1
    return res



def part_2(expr):
    res, op = 0, ''
    i = 0
    while i < len(expr):
        char = expr[i]
        if char == '*':
            return res * part_2(expr[i+1:])
        if char == '(':
            j = matching_bracket(expr, i)
            char = part_2(expr[i+1:j])
            i = j
        elif char.isnumeric():
            char = int(char)
        elif char == '+':
            op = char
        if isinstance(char, int):
            if not op:
                res = char
            elif op == '+':
                res += char
        i += 1
    return res



def do_the_math(data, calc):
    return sum(map(calc, data))

ans_1 = do_the_math(data, part_1)
ans_2 = do_the_math(data, part_2)
print(f'Part 1: {ans_1}')
print(f'Part 2: {ans_2}')