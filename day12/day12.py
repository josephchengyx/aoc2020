import csv
from math import pi, cos, sin
from numpy import array, matmul

with open('day12_input.csv', newline='') as f:
    reader = csv.reader(f)
    data = list()
    for line in reader:
        data.append(line[0])

# print(data[:10])



def part_1(data):
    dirn = ('N', 'E', 'S', 'W')
    deg = 1
    E_dist, N_dist = 0, 0

    for instr in data:
        act, val = instr[0], int(instr[1:])
        if act == 'F':
            act = dirn[deg]
        if act == 'E':
            E_dist += val
        elif act == 'W':
            E_dist -= val
        elif act == 'N':
            N_dist += val
        elif act == 'S':
            N_dist -= val
        elif act == 'R':
            deg += val//90
            while deg >= 4:
                deg -= 4
        elif act == 'L':
            deg -= val//90
            while deg < 0:
                deg += 4

    return E_dist, N_dist



def part_2(data):
    waypt = array([10, 1])
    E_dist, N_dist = 0, 0

    for instr in data:
        act, val = instr[0], int(instr[1:])
        if act == 'F':
            E_dist += val * waypt[0]
            N_dist += val * waypt[1]
        elif act == 'E':
            waypt[0] += val
        elif act == 'W':
            waypt[0] -= val
        elif act == 'N':
            waypt[1] += val
        elif act == 'S':
            waypt[1] -= val
        elif act == 'R' or act == 'L':
            rad = val * pi/180
            if act == 'R':
                rad = -rad
            c, s = int(cos(rad)), int(sin(rad))
            rot = array([[c, -s], [s, c]])
            waypt = matmul(rot, waypt)

    return E_dist, N_dist



def manhattan_dist(E, N):
    return abs(E) + abs(N)



a1_E, a1_N = part_1(data)
ans_1 = manhattan_dist(a1_E, a1_N)
a2_E, a2_N = part_2(data)
ans_2 = manhattan_dist(a2_E, a2_N)
print(f'Part 1: {ans_1}')
print(f'Part 2: {ans_2}')
