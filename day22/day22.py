with open('day22_input.txt', newline='') as f:
    reader = f.read().splitlines()
    data = list()
    for line in reader:
        data.append(line)

# print(data)

def parse(data):
    sp = data.index('')
    player1 = tuple(map(int, data[1:sp]))
    player2 = tuple(map(int, data[sp+2:]))
    return player1, player2

player1, player2 = parse(data)
# print(f"Player 1's deck: {player1}")
# print(f"Player 2's deck: {player2}")



def score(deck):
    N = len(deck)
    res = map(lambda x, y: x * y, deck, range(N, 0 ,-1))
    return sum(res)

def part_1(p1, p2):
    while p1 and p2:
        c1, c2 = p1[0], p2[0]
        p1, p2 = p1[1:], p2[1:]
        if c1 > c2:
            p1 += (c1, c2)
        else:
            p2 += (c2, c1)
    return score(p1) if p1 else score(p2)



def recursive_combat(p1, p2):
    history = set()
    while p1 and p2:
        if (p1, p2) in history:
            return ('p1', p1)

        history.add((p1, p2))
        c1, c2 = p1[0], p2[0]
        p1, p2 = p1[1:], p2[1:]

        if len(p1) >= c1 and len(p2) >= c2:
            rnd = recursive_combat(p1[:c1], p2[:c2])[0]
        elif c1 > c2:
            rnd = 'p1'
        else:
            rnd = 'p2'
        
        if rnd == 'p1':
            p1 += (c1, c2)
        else:
            p2 += (c2, c1)
    
    return ('p1', p1) if p1 else ('p2', p2)

def part_2(p1, p2):
    return score(recursive_combat(p1, p2)[1])



ans_1 = part_1(player1, player2)
ans_2 = part_2(player1, player2)
print(f'Part 1: {ans_1}')
print(f'Part 2: {ans_2}')