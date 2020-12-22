from collections import defaultdict


with open('tests/assertions', 'r') as f:
    assertions = [group.split('\n') for group in f.read().split('\n\n')]


def count_answers(group):
    return len({answer for person in group for answer in person})


def count_intersection_of_answers(group):
    d = defaultdict(set)
    for person in group:
        for answer in person:
            d[person].add(answer)
    return len(set.intersection(*d.values()))


def sum_of_counts(groups, mistake=False):
    if not mistake:
        return sum(count_answers(group) for group in groups)
    else:
        return sum(count_intersection_of_answers(group) for group in groups)


assert sum_of_counts(assertions) == 11
assert sum_of_counts(assertions, mistake=True) == 6


if __name__ == "__main__":
    with open('inputs', 'r') as f:
        groups = [group.split('\n') for group in f.read().split('\n\n')]
    print(sum_of_counts(groups))
    print(sum_of_counts(groups, mistake=True))
