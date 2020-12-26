from functools import reduce


with open('tests/assertions', 'r') as f:
    raw = [s for s in f.read().split('\n') if s]


def process_raw(raw, part_two=False):
    if not part_two:
        return int(raw[0]), [int(n) for n in raw[1].split(',') if n != 'x']
    else:
        raw = [n for n in raw[1].split(',')]
        return [(i, int(n)) for i, n in enumerate(raw) if n != 'x']


def find_bus(depart, buses):
    missed = [depart % bus for bus in buses]
    waits = {bus: bus - miss for bus, miss in zip(buses, missed)}
    bus = min(waits, key=lambda x: waits[x])
    return bus * waits[bus]


'''
    Given this sequence "7, 13, x, x, 59, x, 31, 19", we need to find timestamp t such that:

    t % 7 == 0
    t % 13 == 13 - 1
    -> skip
    -> skip
    t % 59 == 59 - 4
    -> skip
    t % 31 == 31 - 6
    t % 19 == 19 - 7

    One way to solve is by using the Chinese Reminder Theorem, as 7, 13, 59, 31, 19 are coprimes.
    (https://rosettacode.org/wiki/Chinese_remainder_theorem#Python_3.6)
'''


def factors(buses):
    return [(bus, (bus-i) % bus) for i, bus in buses]


def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1


A = process_raw(raw)
assert find_bus(*A) == 295
A = process_raw(raw, part_two=True)
n, a = zip(*factors(A))
assert chinese_remainder(n, a) == 1068781


if __name__ == '__main__':
    with open('inputs', 'r') as f:
        raw = [s for s in f.read().split('\n') if s]
    I = process_raw(raw)
    print(find_bus(*I))
    I = process_raw(raw, part_two=True)
    n, a = zip(*factors(I))
    print(chinese_remainder(n, a))
