with open('tests/assertions') as f:
    assertions1 = f.read().split('\n')


def break_infinite_loop(instructions):
    acc = 0
    idx = 0
    exec_order = set()
    while True:
        if idx in exec_order or idx == len(instructions):
            return acc
        exec_order.add(idx)
        op, arg = instructions[idx].split(' ')
        acc = adjust_acc(acc, op, arg)
        idx = adjust_index(idx, op, arg)


def test_config(instructions):
    idx = 0
    exec_order = set()
    while True:
        if idx in exec_order:
            return False
        if idx == len(instructions):
            return True
        exec_order.add(idx)
        op, arg = instructions[idx].split(' ')
        idx = adjust_index(idx, op, arg)


def fix_corrupt_instruction(instructions):
    config = instructions.copy()
    for i, instruction in enumerate(instructions):
        if instruction.startswith('nop'):
            config[i] = instruction.replace('nop', 'jmp')
            if test_config(config):
                return break_infinite_loop(config)
            else:
                config = instructions.copy()
        if instruction.startswith('jmp'):
            config[i] = instruction.replace('jmp', 'nop')
            if test_config(config):
                return break_infinite_loop(config)
            else:
                config = instructions.copy()


def adjust_acc(acc, op, arg):
    return eval(f'{acc}{arg}') if op == 'acc' else acc


def adjust_index(idx, op, arg):
    if op == 'acc' or op == 'nop':
        return idx + 1
    else:
        return eval(f'{idx}{arg}')


assert break_infinite_loop(assertions1) == 5
assert fix_corrupt_instruction(assertions1) == 8


if __name__ == "__main__":
    with open('inputs', 'r') as f:
        inputs = f.read().split('\n')
    print(break_infinite_loop(inputs))
    print(fix_corrupt_instruction(inputs))
