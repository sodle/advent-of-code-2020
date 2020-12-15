from typing import Any


def all_indices_of(needle: Any, haystack: [Any]):
    return [index for index, item in enumerate(haystack) if item == needle]


def game_loop(starting_numbers):
    spoken_numbers = []
    for n in starting_numbers:
        spoken_numbers.append(n)
        yield n
    while True:
        needle = spoken_numbers[-1]
        haystack = spoken_numbers
        indices = all_indices_of(needle, haystack)
        if len(indices) >= 2:
            second_latest, latest = indices[-2:]
            age = latest - second_latest
            spoken_numbers.append(age)
            yield age
        else:
            spoken_numbers.append(0)
            yield 0


def part1(starting_numbers: [int], target_index: int = 2020) -> int:
    index = 0
    numbers_spoken = game_loop(starting_numbers)
    for number in numbers_spoken:
        index += 1
        if index == target_index:
            return number


def part2(starting_numbers: [int]) -> int:
    return part1(starting_numbers, 30000000)
