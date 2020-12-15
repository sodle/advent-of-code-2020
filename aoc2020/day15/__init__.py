from typing import Any


class IndexCache(object):
    def __init__(self):
        self.indices: {int: [int]} = {}

    def put_index_of(self, value: int, index: int):
        if value in self.indices:
            self.indices[value].append(index)
        else:
            self.indices[value] = [index]

    def get_indices_of(self, value: int):
        return self.indices.get(value, [])


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


def game_loop_v2(starting_numbers):
    index_cache = IndexCache()

    spoken_numbers = []
    for n in starting_numbers:
        index_cache.put_index_of(n, len(spoken_numbers))
        spoken_numbers.append(n)
        yield n
    while True:
        needle = spoken_numbers[-1]
        indices = index_cache.get_indices_of(needle)
        if len(indices) >= 2:
            second_latest, latest = indices[-2:]
            age = latest - second_latest
            index_cache.put_index_of(age, len(spoken_numbers))
            spoken_numbers.append(age)
            yield age
        else:
            index_cache.put_index_of(0, len(spoken_numbers))
            spoken_numbers.append(0)
            yield 0


def part1(starting_numbers: [int], target_index: int = 2020) -> int:
    index = 0
    numbers_spoken = game_loop_v2(starting_numbers)
    for number in numbers_spoken:
        index += 1
        if index == target_index:
            return number


def part2(starting_numbers: [int]) -> int:
    return part1(starting_numbers, 30000000)
