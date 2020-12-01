from pathlib import Path


def read_input(puzzle_filename: str) -> [int]:
    input_filename = Path(puzzle_filename).parent.joinpath('input.txt')
    with open(input_filename) as input_file:
        puzzle_input = input_file.read()
        lines = puzzle_input.split('\n')
        return [int(line) for line in lines if len(line) > 0]
