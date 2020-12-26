with open('tests/assertions', 'r') as f:
    assertions = f.read().split('\n')


def find_id(row, col):
    return row * 8 + col


def find_seat(config):
    row = int(config[:-3].replace('B', '1').replace('F', '0'), 2)
    col = int(config[-3:].replace('R', '1').replace('L', '0'), 2)
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
