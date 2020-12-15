from ..shared import read_input_int_list
from . import part1, part2

if __name__ == "__main__":
    starting_numbers = read_input_int_list(__file__)

    print(f"Part 1: {part1(starting_numbers)}")
    print(f"Part 2: {part2(starting_numbers)}")
