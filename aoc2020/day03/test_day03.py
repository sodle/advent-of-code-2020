import unittest

from . import follow_slope, part1, part2


class Day03(unittest.TestCase):
    sample_input = [
        "..##.......",
        "#...#...#..",
        ".#....#..#.",
        "..#.#...#.#",
        ".#...##..#.",
        "..#.##.....",
        ".#.#.#....#",
        ".#........#",
        "#.##...#...",
        "#...##....#",
        ".#..#...#.#",
    ]

    def test_follow_slope(self):
        assert follow_slope(self.sample_input, 1, 1) == 2
        assert follow_slope(self.sample_input, 3, 1) == 7
        assert follow_slope(self.sample_input, 5, 1) == 3
        assert follow_slope(self.sample_input, 7, 1) == 4
        assert follow_slope(self.sample_input, 1, 2) == 2

    def test_part1(self):
        assert part1(self.sample_input) == 7

    def test_part2(self):
        assert part2(self.sample_input) == 336


if __name__ == '__main__':
    unittest.main()
