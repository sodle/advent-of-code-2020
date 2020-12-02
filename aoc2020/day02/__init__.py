import re

entry_regex = re.compile(r'(\d+)-(\d+) (\w): (\w+)')


def parse_entry(entry: str) -> (int, int, str, str):
    lower, upper, needle, haystack = entry_regex.match(entry).groups()
    return int(lower), int(upper), needle, haystack


def valid_part1(entry: str) -> bool:
    min_occurrences, max_occurrences, needle, haystack = parse_entry(entry)

    occurrences = [c for c in haystack if c == needle]
    num_occurrences = len(occurrences)

    return min_occurrences <= num_occurrences <= max_occurrences


def valid_part2(entry: str) -> bool:
    index_a, index_b, needle, haystack = parse_entry(entry)

    # convert from one-index to zero-index
    char_a = haystack[index_a - 1]
    char_b = haystack[index_b - 1]

    match_a = char_a == needle
    match_b = char_b == needle

    # xor
    return match_a != match_b


def part1(entries: [str]) -> int:
    valid_entries = [e for e in entries if valid_part1(e)]
    return len(valid_entries)


def part2(entries: [int]) -> int:
    valid_entries = [e for e in entries if valid_part2(e)]
    return len(valid_entries)
