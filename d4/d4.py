import re


with open('tests/assertions', 'r') as f:
    assertions = f.read()

with open('tests/valid_passports', 'r') as f:
    ok_passports = f.read()

with open('tests/invalid_passports', 'r') as f:
    nok_passports = f.read()


fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']


def parse_passports(file):
    parsed = [line.replace('\n', ' ').split(' ') for line in file.split('\n\n')]
    passports = []
    for passport in parsed:
        tmp = {}
        for field in passport:
            key, value = field.split(':')
            tmp[key] = value
        passports.append(tmp)
    return passports


def valid_passports(passports, mandatory, check_values=False):
    if not check_values:
        return sum([all(field in passport for field in mandatory) for passport in passports])
    else:
        return sum([all(eval(f"valid_{field}({passport}.get('{field}', ''))") for field in mandatory) for passport in passports])


def valid_byr(value):
    return 1920 <= int(value or 0) <= 2002


def valid_iyr(value):
    return 2010 <= int(value or 0) <= 2020


def valid_eyr(value):
    return 2020 <= int(value or 0) <= 2030


def valid_hgt(value):
    if value.endswith('cm'):
        return 150 <= int(value[:-2]) <= 193
    elif value.endswith('in'):
        return 59 <= int(value[:-2]) <= 76
    else:
        return False


def valid_hcl(value):
    return True if re.match(r'^#[0-9a-f]{6}$', value) else False


def valid_ecl(value):
    return value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


def valid_pid(value):
    return True if re.match(r'^[0-9]{9}$', value) else False


passports = parse_passports(assertions)
assert valid_passports(passports, fields) == 2
passports = parse_passports(ok_passports)
assert valid_passports(passports, fields, check_values=True) == 4
passports = parse_passports(nok_passports)
assert valid_passports(passports, fields, check_values=True) == 0


if __name__ == "__main__":
    with open('inputs', 'r') as f:
        inputs = f.read()
    passports = parse_passports(inputs)
    print(valid_passports(passports, fields))
    print(valid_passports(passports, fields, check_values=True))
