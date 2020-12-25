with open('tests/assertions') as f:
    assertions = [int(x) for x in f.read().split('\n')]


def chain_adapters(adapters):
    adapters = adjust_jolts(adapters)
    jolt_diff = {1: 0, 3: 0}
    i, j = 0, 1
    while j < len(adapters):
        jolt_diff[adapters[j] - adapters[i]] += 1
        i += 1
        j += 1
    return jolt_diff


def adjust_jolts(adapters):
    adapters.append(0)
    adapters.append(max(adapters)+3)
    return sorted(adapters)


# dynamic programming
def find_arrangements(i):
    if i == len(ADAPTERS) - 1:
        return 1
    if i in STACK:
        return STACK[i]
    ans = 0
    for j in range(i+1, len(ADAPTERS)):
        if ADAPTERS[j] - ADAPTERS[i] <= 3:
            ans += find_arrangements(j)
    STACK[i] = ans
    return ans


assert chain_adapters(assertions.copy()) == {1: 22, 3: 10}
ADAPTERS = adjust_jolts(assertions.copy())
STACK = {}
assert find_arrangements(0) == 19208


if __name__ == "__main__":
    with open('inputs') as f:
        inputs = [int(x) for x in f.read().split('\n')]
    print(chain_adapters(inputs))
    ADAPTERS = adjust_jolts(inputs.copy())
    STACK = {}
    print(find_arrangements(0))
