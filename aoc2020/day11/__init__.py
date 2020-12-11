from typing import Optional


def get_surrounding_indexes(grid: [[str]], row: int, col: int) -> [(int, int)]:
    num_rows = len(grid)
    num_cols = len(grid[row])

    go_left = col > 0
    go_up = row > 0
    go_right = col < num_cols - 1
    go_down = row < num_rows - 1

    if go_up:
        yield row - 1, col
        if go_left:
            yield row - 1, col - 1
        if go_right:
            yield row - 1, col + 1
    if go_down:
        yield row + 1, col
        if go_left:
            yield row + 1, col - 1
        if go_right:
            yield row + 1, col + 1
    if go_left:
        yield row, col - 1
    if go_right:
        yield row, col + 1


def gaze_up(grid: [[str]], row: int, col: int) -> Optional[str]:
    row -= 1
    while row >= 0:
        if grid[row][col] != ".":
            return grid[row][col]
        row -= 1


def gaze_down(grid: [[str]], row: int, col: int) -> Optional[str]:
    row += 1
    while row < len(grid):
        if grid[row][col] != ".":
            return grid[row][col]
        row += 1


def gaze_left(grid: [[str]], row: int, col: int) -> Optional[str]:
    col -= 1
    while col >= 0:
        if grid[row][col] != ".":
            return grid[row][col]
        col -= 1


def gaze_right(grid: [[str]], row: int, col: int) -> Optional[str]:
    col += 1
    while col < len(grid[row]):
        if grid[row][col] != ".":
            return grid[row][col]
        col += 1


def gaze_up_left(grid: [[str]], row: int, col: int) -> Optional[str]:
    row -= 1
    col -= 1
    while row >= 0 and col >= 0:
        if grid[row][col] != ".":
            return grid[row][col]
        row -= 1
        col -= 1


def gaze_up_right(grid: [[str]], row: int, col: int) -> Optional[str]:
    row -= 1
    col += 1
    while row >= 0 and col < len(grid[row]):
        if grid[row][col] != ".":
            return grid[row][col]
        row -= 1
        col += 1


def gaze_down_left(grid: [[str]], row: int, col: int) -> Optional[str]:
    row += 1
    col -= 1
    while row < len(grid) and col >= 0:
        if grid[row][col] != ".":
            return grid[row][col]
        row += 1
        col -= 1


def gaze_down_right(grid: [[str]], row: int, col: int) -> Optional[str]:
    row += 1
    col += 1
    while row < len(grid) and col < len(grid[row]):
        if grid[row][col] != ".":
            return grid[row][col]
        row += 1
        col += 1


def evaluate_seat(grid: [[str]], row: int, col: int) -> str:
    seat = grid[row][col]

    if seat == ".":
        return seat

    surrounding = [grid[r][c] for r, c in get_surrounding_indexes(grid, row, col)]
    occupied_surrounding = len([seat for seat in surrounding if seat == "#"])

    if seat == "L" and occupied_surrounding == 0:
        return "#"
    if seat == "#" and occupied_surrounding >= 4:
        return "L"
    return seat


def evaluate_seat_part2(grid: [[str]], row: int, col: int) -> str:
    seat = grid[row][col]

    if seat == ".":
        return seat

    surrounding = [
        gaze_up_left(grid, row, col),
        gaze_up(grid, row, col),
        gaze_up_right(grid, row, col),
        gaze_left(grid, row, col),
        gaze_right(grid, row, col),
        gaze_down_left(grid, row, col),
        gaze_down(grid, row, col),
        gaze_down_right(grid, row, col),
    ]
    occupied_surrounding = len([seat for seat in surrounding if seat == "#"])

    if seat == "L" and occupied_surrounding == 0:
        return "#"
    if seat == "#" and occupied_surrounding >= 5:
        return "L"
    return seat


def evaluate_row(grid: [[str]], row: int, is_part_2: bool = False) -> [str]:
    seat_function = evaluate_seat_part2 if is_part_2 else evaluate_seat
    return [seat_function(grid, row, col) for col in range(len(grid[row]))]


def evaluate_grid(grid: [[str]], is_part_2: bool = False) -> [[str]]:
    return [evaluate_row(grid, row, is_part_2) for row in range(len(grid))]


def count_occupied(grid: [[str]]) -> int:
    return sum([len([seat for seat in row if seat == "#"]) for row in grid])


def print_grid(grid: [[str]]):
    print()
    print("\n".join("".join(row) for row in grid))
    print()


def part1(puzzle_input: [[str]]) -> int:
    current_grid = puzzle_input
    new_grid = evaluate_grid(current_grid)
    while current_grid != new_grid:
        current_grid = new_grid
        new_grid = evaluate_grid(current_grid)
    return count_occupied(current_grid)


def part2(puzzle_input: [[str]]) -> int:
    current_grid = puzzle_input
    new_grid = evaluate_grid(current_grid, is_part_2=True)
    while current_grid != new_grid:
        current_grid = new_grid
        new_grid = evaluate_grid(current_grid, is_part_2=True)
    return count_occupied(current_grid)
