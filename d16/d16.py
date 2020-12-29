from collections import defaultdict


with open('tests/assertions', 'r') as f:
    raw = f.read().split('\n\n')


def parse_ticket(raw):
    tickets, rules = {}, defaultdict(dict)
    for fs in raw:
        if fs.startswith('your'):
            tickets['mine'] = [int(i) for i in fs.split('\n')[-1].split(',')]
        elif fs.startswith('nearby'):
            tickets['nearby'] = [[int(i) for i in ts.split(',') if i.strip()] for ts in fs.split(':\n')[-1].split('\n') if ts]
        else:
            for f in fs.split('\n'):
                n, vals = f.split(': ')
                lb, ub = vals.split(' or ')
                rules[n]['lb'] = [int(i) for i in lb.split('-')]
                rules[n]['ub'] = [int(i) for i in ub.split('-')]
    return tickets, rules


def error_rate(tickets, rules, discard=False):
    invalid = []
    to_discard = []
    c = 0
    for t in tickets['nearby']:
        for v in t:
            is_valid = False
            for f in rules.keys():
                lb, ub = rules[f]['lb'], rules[f]['ub']
                if lb[0] <= v <= lb[1] or ub[0] <= v <= ub[1]:
                    is_valid = True
            if not is_valid:
                    invalid.append(v)
                    to_discard.append(t)
    return sum(invalid) if not discard else to_discard


def decipher_ticket(tickets, rules):
    order = defaultdict(set)
    dont_use = error_rate(tickets, rules, discard=True)
    valid_tickets = [t for t in tickets['nearby'] if t not in dont_use]
    for i in range(len(rules)):
        vs = [t[i] for t in valid_tickets]
        for f in rules.keys():
            ok = True
            for v in vs:
                lb, ub = rules[f]['lb'], rules[f]['ub']
                if not (lb[0] <= v <= lb[1] or ub[0] <= v <= ub[1]):
                    ok = False
            if ok:
                order[f].add(i)

    mapping = {}
    remove = set()
    for i in range(len(rules)):
        for f, vs in order.items():
            vs -= remove
            if len(vs) == 1:
                pos = vs.pop()
                mapping[f] = pos
                remove.add(pos)

    p = 1
    for f in mapping:
        if f.startswith('departure'):
            p *= tickets['mine'][mapping[f]]
    return p


assert error_rate(*parse_ticket(raw)) == 71


if __name__ == '__main__':
    with open('inputs', 'r') as f:
        raw = f.read().split('\n\n')
    print(error_rate(*parse_ticket(raw)))
    print(decipher_ticket(*parse_ticket(raw)))
