from functools import reduce
from pathlib import Path


def read_input_numbers(puzzle_filename: str, preserve_newlines=False) -> [int]:
    lines = read_input_strings(puzzle_filename, preserve_newlines)
    return [int(line) for line in lines]


def read_input_strings(puzzle_filename: str, preserve_newlines=False) -> [str]:
    input_filename = Path(puzzle_filename).parent.joinpath('input.txt')
    with open(input_filename) as input_file:
        puzzle_input = input_file.read()
        lines = puzzle_input.split('\n')
        return [line for line in lines if len(line) > 0 or preserve_newlines]


def read_input_int_list(puzzle_filename: str) -> [int]:
    line, = read_input_strings(puzzle_filename)
    return [int(n) for n in line.split(",")]


def cumulative_product(terms: [int]) -> int:
    return reduce(lambda a, b: a * b, terms)


def split_on_blank_lines(lines: [str]) -> [str]:
    batch = []
    for line in lines:
        if len(line) == 0:
            if len(batch) > 0:
                yield batch
            batch = []
        else:
            batch.append(line)
    if len(batch) > 0:
        yield batch
