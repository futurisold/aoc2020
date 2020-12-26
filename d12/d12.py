with open('tests/assertions', 'r') as f:
    assertions = [(a[0], int(a[1:])) for a in f.read().split('\n') if a]


def navigate(actions):
    x, y = 0, 0
    direction  = 0

    for action, amount in actions:
        if action == 'N':
            y += amount
        elif action == 'S':
            y -= amount
        elif action == 'E':
            x += amount
        elif action == 'W':
            x -= amount
        elif action == 'L':
            direction = (direction + amount) % 360
        elif action == 'R':
            direction = (direction - amount) % 360
        elif action == 'F':
            if direction == 0:
                x += amount
            elif direction == 90:
                y += amount
            elif direction == 180:
                x -= amount
            else:
                y -= amount
    return abs(x) + abs(y)


def navigate_relative_to_waypoint(actions):
    x, y = 0, 0
    wp_x, wp_y = 10, 1
    direction = 0

    for action, amount in actions:
        if action == 'N':
            wp_y += amount
        elif action == 'S':
            wp_y -= amount
        elif action == 'E':
            wp_x += amount
        elif action == 'W':
            wp_x -= amount
        elif action == 'L':
            for _ in range(amount // 90):
                wp_x, wp_y = -wp_y, wp_x
        elif action == 'R':
            for _ in range(amount // 90):
                wp_x, wp_y = wp_y, -wp_x
        else:
            x += wp_x * amount
            y += wp_y * amount
    return abs(x) + abs(y)


assert navigate(assertions) == 25
assert navigate_relative_to_waypoint(assertions) == 286


if __name__ == '__main__':
    with open('inputs', 'r') as f:
        inputs = [(a[0], int(a[1:])) for a in f.read().split('\n') if a]
        print(navigate(inputs))
        print(navigate_relative_to_waypoint(inputs))
