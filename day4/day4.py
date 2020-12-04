import re

with open("input.txt") as file:
    lines = [lines.replace("\n", " ") for lines in file.read().split("\n\n")]

passports = [{key: value for word in line.split() for key, value in [word.split(':')]} for line in lines]

mandatory = ['byr', 'pid', 'eyr', 'iyr', 'hgt', 'hcl', 'ecl']

valid_passports = []
for passport in passports:
    keys = list(passport.keys())

    if 'cid' in keys:
        keys.remove('cid')

    if set(keys) == set(mandatory):
        valid_passports.append(passport)

print(len(valid_passports))

# part 2

def valid_year(year):
    return re.search('^[0-9]{4}$', year)
def is_in_range(min, max, value):
    return min <= value <= max
def is_color(color):
    return re.search('^#[a-f0-9]{6}$', color)
def is_ecl(ecl):
    return ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
def is_pid(pid):
    return re.search('^[0-9]{9}$', pid)
def is_height(height):
    measure_unit = re.findall('cm|in$', height)

    if(measure_unit):
        h = int(re.split(measure_unit[0], height)[0])

        if (measure_unit[0] == 'cm' and 150 <= h <= 193) or (measure_unit[0] == 'in' and 59 <= h <= 76):
            return True

    return False


def validator(passport):
    if (not valid_year(passport['byr']) or not is_in_range(1920, 2020, int(passport['byr']))) or \
            (not valid_year(passport['iyr']) or not is_in_range(2010, 2020, int(passport['iyr']))) or \
            (not valid_year(passport['eyr']) or not is_in_range(2020, 2030, int(passport['eyr']))) or \
            not is_ecl(passport['ecl']) or not is_color(passport['hcl']) or not is_pid(passport['pid']) or \
            not is_height(passport['hgt']):
        return False

    return True

print(sum([validator(passport) for passport in valid_passports]))
