with open('tests/assertions', 'r') as f:
    assertions = [int(line) for line in f]


def find_prod_2(values):
    for x in values:
        for y in values[::-1]:
            if x + y == 2020:
                return x * y


assert find_prod_2(assertions) == 514579


def find_prod_3(values):
    sum_2 = {}
    for x in values:
        for y in values[::-1]:
            sum_2[x + y] = x * y
    for x in values:
        for y in sum_2.keys():
            if x + y == 2020:
                return x * sum_2[y]


assert find_prod_3(assertions) == 241861950


if __name__ == "__main__":
    with open('inputs', 'r') as f:
        inputs = [int(line) for line in f]
        print(find_prod_2(inputs), find_prod_3(inputs))
