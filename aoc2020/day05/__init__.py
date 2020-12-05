def find_seat(seat_code: str) -> (int, int):
    rows = list(range(128))
    cols = list(range(8))

    for char in seat_code:
        if char == "F":
            rows = rows[:len(rows) // 2]
        elif char == "B":
            rows = rows[len(rows) // 2:]
        elif char == "L":
            cols = cols[:len(cols) // 2]
        elif char == "R":
            cols = cols[len(cols) // 2:]

    return rows[0], cols[0]


def seat_id(seat_code: str) -> int:
    row, col = find_seat(seat_code)
    return 8 * row + col


def part1(lines: [str]) -> int:
    seat_ids = [seat_id(line) for line in lines]
    return max(seat_ids)


def part2(lines: [str]) -> int:
    seat_ids = [seat_id(line) for line in lines]
    seat_ids.sort()

    for seat in seat_ids:
        if (seat + 1) not in seat_ids and (seat + 2) in seat_ids:
            return seat + 1
