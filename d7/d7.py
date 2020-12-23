from collections import defaultdict
import re


with open('tests/assertions1', 'r') as f:
    assertions1 = f.read().split('\n')

with open('tests/assertions2', 'r') as f:
    assertions2 = f.read().split('\n')


def parse_rules(rules):
    bags = defaultdict(dict)
    for rule in rules:
        rule = re.sub(r'\sbags?[.\s]?', '', rule)
        bag_color, subbags = rule.split('contain ')
        for subbag in subbags.split(', '):
            subbag_color = re.findall(r'\D+', subbag).pop().lstrip()
            if subbag_color == 'no other':
                bags[bag_color] = {}
            else:
                n = int(re.findall(r'\d', subbag)[0])
                bags[bag_color][subbag_color] = n
    return bags


def find_parents(bags):
    parents = defaultdict(list)
    for st_bag in bags:
        for nd_bag in bags[st_bag]:
            parents[nd_bag].append(st_bag)
    return parents


def find_outermost_bags(bags, color):
    parents = find_parents(bags)
    to_check = [color]
    outermost_bags = set()
    while to_check:
        child = to_check.pop()
        for parent in parents.get(child, []):
            if parent not in outermost_bags:
                outermost_bags.add(parent)
                to_check.append(parent)
    return len(outermost_bags)


def count_individual_bags(bags, color):
    to_check = [(color, 1)]
    total = 0
    while to_check:
        parent, multiplier = to_check.pop()
        for child, count in bags[parent].items():
            total += multiplier * count
            to_check.append((child, multiplier * count))
    return total


bags = parse_rules(assertions1)
assert find_outermost_bags(bags, 'shiny gold') == 4
bags = parse_rules(assertions2)
assert count_individual_bags(bags, 'shiny gold') == 126
count_individual_bags(bags, 'shiny gold')

if __name__ == "__main__":
    with open('inputs', 'r') as f:
        inputs = f.read().split('\n')
    inputs = parse_rules(inputs)
    print(find_outermost_bags(inputs, 'shiny gold'))
    print(count_individual_bags(inputs, 'shiny gold'))
