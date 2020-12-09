from ..shared import read_input_numbers
from . import part1, part2

if __name__ == "__main__":
    puzzle_input = read_input_numbers(__file__)

    part_1 = part1(puzzle_input)
    print(f"Part 1: {part_1}")
    print(f"Part 2: {part2(puzzle_input, part_1)}")
