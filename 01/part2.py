def read_input() -> [int]:
    with open('input.txt') as input_file:
        puzzle_input = input_file.read()
        lines = puzzle_input.split('\n')
        return [int(line) for line in lines if len(line) > 0]


def main():
    expenses = read_input()
    for e1 in expenses:
        for e2 in expenses:
            for e3 in expenses:
                if e1 + e2 + e3 == 2020:
                    print(f"{e1 * e2 * e3}")
                    return


if __name__ == "__main__":
    main()
