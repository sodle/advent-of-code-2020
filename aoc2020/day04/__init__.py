import re


def split_on_blank_lines(lines: [str]) -> [str]:
    batch = []
    for line in lines:
        if len(line) == 0:
            if len(batch) > 0:
                yield batch
            batch = []
        else:
            batch.append(line)
    if len(batch) > 0:
        yield batch


def parse_passport(lines: [str]) -> dict:
    passport = {}
    for line in lines:
        fields = line.split(' ')
        for field in fields:
            key, value = field.split(':')
            passport[key] = value
    return passport


def is_passport_valid(passport: dict) -> bool:
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for field in required_fields:
        if field not in passport:
            return False
    return True


def strict_passport_check(passport: dict) -> bool:
    birth_year = passport.get('byr', '0')
    if not 1920 <= int(birth_year) <= 2002:
        return False

    issue_year = passport.get('iyr', '0')
    if not 2010 <= int(issue_year) <= 2020:
        return False

    exp_year = passport.get('eyr', '0')
    if not 2020 <= int(exp_year) <= 2030:
        return False

    height = passport.get('hgt', '')
    height_match = re.match(r'^(\d+)(cm|in)$', height)
    if height_match:
        value, unit = height_match.groups()
        int_value = int(value)
        if unit == 'cm' and not 150 <= int_value <= 193:
            return False
        if unit == 'in' and not 59 <= int_value <= 76:
            return False
    else:
        return False

    hair_color = passport.get('hcl', '')
    hair_match = re.match(r'^#[0-9a-f]{6}$', hair_color)
    if hair_match is None:
        return False

    eye_color = passport.get('ecl', '')
    if eye_color not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return False

    passport_id = passport.get('pid', '')
    pid_match = re.match(r'^\d{9}$', passport_id)
    if pid_match is None:
        return False

    return True


def part1(rows: [str]) -> int:
    passports = split_on_blank_lines(rows)
    parsed_passports = [parse_passport(p) for p in passports]
    valid_passports = [p for p in parsed_passports if is_passport_valid(p)]
    return len(valid_passports)


def part2(rows: [str]) -> int:
    passports = split_on_blank_lines(rows)
    parsed_passports = [parse_passport(p) for p in passports]
    valid_passports = [p for p in parsed_passports if strict_passport_check(p)]
    return len(valid_passports)
