def sum_in(target_slice: [int], target_sum: int) -> bool:
    for a in target_slice:
        for b in target_slice:
            if a + b == target_sum:
                return True

    return False


def part1(puzzle_input: [int], preamble_length: int = 25) -> int:
    for idx, number in enumerate(puzzle_input):
        if idx < preamble_length:
            pass
        elif sum_in(puzzle_input[idx - preamble_length:idx], number):
            pass
        else:
            return number


def part2(puzzle_input: [int], target: int) -> int:
    for i in range(len(puzzle_input)):
        for j in range(len(puzzle_input) + 1):
            ij_range = puzzle_input[i:j]
            if sum(ij_range) == target:
                return min(ij_range) + max(ij_range)
