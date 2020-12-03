from functools import reduce
from pathlib import Path


def read_input_numbers(puzzle_filename: str) -> [int]:
    lines = read_input_strings(puzzle_filename)
    return [int(line) for line in lines]


def read_input_strings(puzzle_filename: str) -> [str]:
    input_filename = Path(puzzle_filename).parent.joinpath('input.txt')
    with open(input_filename) as input_file:
        puzzle_input = input_file.read()
        lines = puzzle_input.split('\n')
        return [line for line in lines if len(line) > 0]


def cumulative_product(terms: [int]) -> int:
    return reduce(lambda a, b: a * b, terms)
