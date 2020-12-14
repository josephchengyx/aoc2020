from math import prod

with open('day13_input.txt', newline='') as f:
    reader = f.read().splitlines()
    data = list()
    for line in reader:
        data.append(line)
    
# print(data)

t0 = int(data[0])
schedule = data[1].split(',')
buses = list()
for bus in schedule:
    if bus != 'x':
        bus = int(bus)
    buses.append(bus)
active_buses = list(filter(lambda bus: bus != 'x', buses))

# print(t0)
# print(buses)
# print(active_buses)



def part_1(buses, t0):
    earliest_times = list()
    for bus in buses:
        n = int(t0//bus)
        t = (n+1) * bus
        earliest_times.append(t-t0)
    
    t_min, idx = earliest_times[0], 0
    for i in range(1, len(earliest_times)):
        t = earliest_times[i]
        if t < t_min:
            t_min = t
            idx = i

    return buses[idx], t_min



def gcdExtended(a, b):
    if a == 0:
        return b, 0, 1
    
    gcd, x1, y1 = gcdExtended(b%a, a)
    x = y1 - (b//a) * x1
    y = x1

    return gcd, x, y

def part_2(buses):
    eqns = list()
    for i in range(len(buses)):
        bus = buses[i]
        if bus != 'x':
            eqns.append((bus, -i))
    
    # chinese remainder theorem magic
    N = prod(map(lambda tup: tup[0], eqns))
    res = 0
    for n, r in eqns:
        y = N//n
        gcd, z, k = gcdExtended(y, n)
        res += r * y * z
    
    return res % N



busID_1, tmin_1 = part_1(active_buses, t0)
ans_1 = busID_1 * tmin_1
ans_2 = part_2(buses)
print(f'Part 1: {ans_1}')
print(f'Part 2: {ans_2}')