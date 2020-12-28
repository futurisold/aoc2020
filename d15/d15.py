A = [0, 3, 6]


def memory_game(ns, r):
    stack = {}
    for i, n in enumerate(ns[:-1]):
        stack[n] = i
    while len(ns) < r:
        prev = ns[-1]
        pprev = stack.get(prev, -1)
        stack[prev] = len(ns) - 1
        if pprev == -1:
            nxt = 0
        else:
            # the len of the current list is the last idx
            # from which we subtract the pprev idx
            nxt = len(ns) - 1 - pprev
        ns.append(nxt)
    return ns[-1]


assert memory_game(A, 10) == 0
assert memory_game(A, 2020) == 436
assert memory_game(A, 30000000) == 175594

if __name__ == '__main__':
    I = [6,13,1,15,2,0]
    print(memory_game(I, 2020))
    print(memory_game(I, 30000000))
