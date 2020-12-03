from aoc2020.shared import cumulative_product


def follow_slope(rows: [str], right: int, down: int) -> int:
    x = 0
    y = 0

    # width of each row
    width = len(rows[0])

    trees = 0
    while y < len(rows):
        if rows[y][x] == '#':
            trees += 1

        # move down, and to the right, wrapping around the right edge if necessary
        y += down
        x = (x + right) % width

    return trees


def part1(rows: [str]) -> int:
    return follow_slope(rows, 3, 1)


def part2(rows: [str]) -> int:
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    tree_counts = [follow_slope(rows, *slope) for slope in slopes]
    return cumulative_product(tree_counts)
