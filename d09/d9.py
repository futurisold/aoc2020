with open('tests/assertions', 'r') as f:
    assertions = [int(x) for x in f.read().split('\n')]


def find_exploit(numbers, preamble):
    i, j = 0, 0
    while j+preamble < len(numbers):
        stack = []
        for n in numbers[i:j+preamble]:
            stack.append(numbers[j+preamble] - n)
        if all([n not in numbers[i:j+preamble] for n in stack]):
            return numbers[j+preamble]
        i += 1
        j += 1


def find_encryption_weakness(numbers, preamble):
    exploit_this = find_exploit(numbers, preamble)
    of_interest = numbers.index(exploit_this)
    seq = numbers[:of_interest]
    curr_sum = seq[0]
    i, j = 0, 1
    while j <= len(seq):
        while curr_sum > exploit_this and i < j-1:
            curr_sum -= seq[i]
            i += 1
        if curr_sum == exploit_this:
            return min(seq[i:j]) + max(seq[i:j])
        if j < len(seq):
            curr_sum += seq[j]
        j += 1


assert find_exploit(assertions, 5) == 127
assert find_encryption_weakness(assertions, 5) == 62


if __name__ == "__main__":
    with open('inputs', 'r') as f:
        inputs = [int(x) for x in f.read().split('\n')]
    print(find_exploit(inputs, 25))
    print(find_encryption_weakness(inputs, 25))
