from collections import defaultdict


with open('assertions', 'r') as f:
    assertions = [line.strip() for line in f]


def parser(lines):
    passwords = defaultdict(dict)
    for i, line in enumerate(lines):
        rg, letter, psw = line.split(' ')
        mn, mx = rg.split('-')
        passwords[i]['rg'] = (int(mn), int(mx))
        passwords[i]['lt'] = letter.split(':')[0]
        passwords[i]['psw'] = psw
    return passwords


def policy_1(passwords):
    valid = []
    for p in passwords:
        cond = 1 if passwords[p]['rg'][0] <= passwords[p]['psw'].count(passwords[p]['lt']) <= passwords[p]['rg'][1] else 0
        valid.append(cond)
    return sum(valid)


def policy_2(passwords):
    valid = []
    for p in passwords:
        i_mn, i_mx = passwords[p]['rg']
        cond_1 = True if (passwords[p]['psw'][i_mn-1] == passwords[p]['lt'] or passwords[p]['psw'][i_mx-1] == passwords[p]['lt']) else False
        cond_2 = 1 if (cond_1 and not passwords[p]['psw'][i_mn-1] == passwords[p]['lt'] == passwords[p]['psw'][i_mx-1] == passwords[p]['lt']) else 0
        valid.append(cond_2)
    return sum(valid)


assert policy_1(parser(assertions)) == 2
assert policy_2(parser(assertions)) == 1


if __name__ == "__main__":
    with open('inputs', 'r') as f:
        inputs = [line.strip() for line in f]
    print(policy_1(parser(inputs)))
    print(policy_2(parser(inputs)))
