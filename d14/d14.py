import itertools


with open('tests/assertions1', 'r') as f:
    A1 = [s for s in f.read().split('\n') if s.strip()]


with open('tests/assertions2', 'r') as f:
    A2 = [s for s in f.read().split('\n') if s.strip()]


def init_program(program, v2=False):
    mask = None
    mem = {}
    for step in program:
        if step.startswith('mask'):
            mask = step.split('= ')[-1][::-1]
        if step.startswith('mem'):
            _ = step.split(' = ')
            mem_adr, val = int(_[0].split('mem[')[-1][:-1]), int(_[1])
            if not v2:
                mem[mem_adr] = update_value_v1(mask, val)
            else:
                mem_adrs = memory_address_decoder(mask, mem_adr)
                for adr in mem_adrs:
                    mem[adr] = val
    return sum(mem.values())


def update_value_v1(mask, val):
    bin_val = format(val, 'b')[::-1]
    i = 0
    new_val = 0
    while i < len(mask):
        while i < len(bin_val):
            if mask[i] == '0':
                new_val += 0
            elif mask[i] == '1':
                new_val += 2**i
            else:
                new_val += 2**i * int(bin_val[i])
            i += 1
        if mask[i] == '1':
            new_val += 2**i
        i += 1
    return new_val


def memory_address_decoder(mask, mem_adr):
    bin_mem_adr = format(mem_adr, 'b')[::-1]
    i = 0
    floating_mask = ''
    while i < len(mask):
        while i < len(bin_mem_adr):
            if mask[i] == 'X':
                floating_mask += 'X'
            elif mask[i] == '0':
                floating_mask += bin_mem_adr[i]
            else:
                floating_mask += '1'
            i += 1
        if mask[i] == '1':
            floating_mask += '1'
        elif mask[i] == '0':
            floating_mask += '0'
        else:
            floating_mask += 'X'
        i += 1
    return cartesian_prod(floating_mask)


def cartesian_prod(floating_mask):
    mem_adrs = []
    for choice in itertools.product(*[[0, 1] for _ in range(floating_mask.count('X'))]):
        update_this = floating_mask
        for bit in choice:
            idx = update_this.index('X')
            update_this = update_this[:idx] + f'{bit}' + update_this[idx+1:]
        mem_adrs.append(int(update_this[::-1], 2))
    return mem_adrs


assert init_program(A1) == 165
assert init_program(A2, v2=True) == 208


if __name__ == '__main__':
    with open('inputs', 'r') as f:
        I = [s for s in f.read().split('\n') if s.strip()]
        print(init_program(I))
        print(init_program(I, v2=True))
