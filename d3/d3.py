with open('assertions', 'r') as f:
    assertions = [line.strip() for line in f]


def parse_map(map, right, down):
    _dstep = down
    _rstep = right
    height = len(map)
    width = len(map[0])
    trees = []
    while height > down:
        tree = 1 if map[down][right % width] == '#' else 0
        trees.append(tree)
        right += _rstep
        down += _dstep
    return sum(trees)


def find_prod(map, slopes):
    p = 1
    for slope in slopes:
        right, down = slope
        p *= parse_map(map, right, down)
    return p


assert parse_map(assertions, 3, 1) == 7
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
assert find_prod(assertions, slopes) == 336


if __name__ == "__main__":
    with open('inputs', 'r') as f:
        inputs = [line.strip() for line in f]
    print(parse_map(inputs, 3, 1))
    print(find_prod(inputs, slopes))