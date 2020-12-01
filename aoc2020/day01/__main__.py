from ..shared import read_input


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


if __name__ == "__main__":
    puzzle_input = read_input(__file__)

    print(f"Part 1: {part1(puzzle_input)}")
    print(f"Part 2: {part2(puzzle_input)}")
