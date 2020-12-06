from ..shared import read_input_strings, split_on_blank_lines
from . import part1, part2

if __name__ == "__main__":
    puzzle_input = read_input_strings(__file__, preserve_newlines=True)
    groups = list(split_on_blank_lines(puzzle_input))

    print(f"Part 1: {part1(groups)}")
    print(f"Part 2: {part2(groups)}")
