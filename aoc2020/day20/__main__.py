from ..shared import read_input_strings
from . import part1, part2

if __name__ == "__main__":
    expressions = read_input_strings(__file__)

    print(f"Part 1: {part1(expressions)}")
    print(f"Part 2: {part2(expressions)}")
