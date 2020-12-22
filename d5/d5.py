with open('tests/assertions', 'r') as f:
    assertions = f.read().split('\n')


def find_id(row, col):
    return row * 8 + col


def find_seat(config):
    row, col = 0, 0
    for i, r in enumerate(config[:-3]):
        step = 2 ** (6 - i)
        upper = 1 if r == 'B' else 0
        row += step * upper
    for i, c in enumerate(config[-3:]):
        step = 2 ** (2 - i)
        upper = 1 if c == 'R' else 0
        col += step * upper
    return row, col


def highest_id(board):
    return max([find_id(*find_seat(config)) for config in board])


def my_id(board):
    seats = [find_id(*find_seat(config)) for config in board]
    mn, mx = min(seats), max(seats)
    return [n for n in range(mn, mx) if n not in seats and n+1 in seats and n-1 in seats].pop()


assert [find_id(*find_seat(config)) for config in assertions] == [567, 119, 820]
assert highest_id(assertions) == 820


if __name__ == "__main__":
    with open('inputs', 'r') as f:
        board = f.read().split('\n')
    print(highest_id(board))
    print(my_id(board))
