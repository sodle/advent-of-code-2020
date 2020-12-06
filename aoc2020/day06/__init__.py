def count_group(lines: [str]) -> int:
    answers = ''.join(lines)
    return len(set(answers))


def count_union_group(lines: [str]) -> int:
    answer_sets = [set(line) for line in lines]
    return len(set.intersection(*answer_sets))


def part1(groups: [[str]]) -> int:
    group_counts = [count_group(group) for group in groups]
    return sum(group_counts)


def part2(groups: [[str]]) -> int:
    group_counts = [count_union_group(group) for group in groups]
    return sum(group_counts)
