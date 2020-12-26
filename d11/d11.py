from collections import Counter


with open('tests/assertions') as f:
    assertions = [list(x) for x in f.read().split('\n')]

NEIGHBORS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def map_layout(grid, first_seat=False):
    r, c = len(grid), len(grid[0])
    return [[update_seat(grid, i, j, first_seat=first_seat) for j in range(c)] for i in range(r)]


def update_seat(grid, i, j, first_seat=False):
    if not first_seat:
        r, c = len(grid), len(grid[0])
        counter = Counter(grid[i+di][j+dj] for di, dj in NEIGHBORS if 0 <= i+di < r and 0 <= j+dj < c)
        curr = grid[i][j]
        if curr == 'L' and counter['#'] == 0:
            return '#'
        if curr == '#' and counter['#'] >= 4:
            return 'L'
        return curr
    else:
        counter = Counter(spot_first_seat(grid, i, j, di, dj) for di, dj in NEIGHBORS)
        curr = grid[i][j]
        if curr == 'L' and counter['#'] == 0:
            return '#'
        if curr == '#' and counter['#'] >= 5:
            return 'L'
        return curr


def spot_first_seat(grid, i, j, di, dj):
    r, c = len(grid), len(grid[0])
    while True:
        i += di
        j += dj
        if 0 <= i < r and 0 <= j < c:
            curr = grid[i][j]
            if curr != '.':
                return curr
        else:
            return '.'


def final_config(grid, first_seat=False):
    while True:
        new_grid = map_layout(grid, first_seat=first_seat)
        if new_grid == grid:
            break
        grid = new_grid
    return total_seats(grid)


def total_seats(grid):
    return sum(seat == '#' for row in grid for seat in row)


assert final_config(assertions) == 37
assert final_config(assertions, first_seat=True) == 26


if __name__ == "__main__":
    with open('inputs', 'r') as f:
        inputs = [list(x) for x in f.read().split('\n')]
    print(final_config(inputs))
    print(final_config(inputs, first_seat=True))
