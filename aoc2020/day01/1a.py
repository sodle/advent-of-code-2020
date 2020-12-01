from ..shared import read_input


def main():
    expenses = read_input()
    for e1 in expenses:
        for e2 in expenses:
            if e1 + e2 == 2020:
                print(f"{e1 * e2}")
                return


if __name__ == "__main__":
    main()
