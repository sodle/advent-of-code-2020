def read_input() -> [int]:
    with open('input.txt') as input_file:
        puzzle_input = input_file.read()
        lines = puzzle_input.split('\n')
        return [int(line) for line in lines if len(line) > 0]
