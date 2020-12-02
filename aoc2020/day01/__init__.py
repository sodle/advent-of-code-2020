def part1(expenses: [int]) -> int:
    for e1 in expenses:
        for e2 in expenses:
            if e1 + e2 == 2020:
                return e1 * e2


def part2(expenses: [int]) -> int:
    for e1 in expenses:
        for e2 in expenses:
            for e3 in expenses:
                if e1 + e2 + e3 == 2020:
                    return e1 * e2 * e3
