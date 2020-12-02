import unittest

from . import part1, part2


class Day02(unittest.TestCase):
    sample_input = [
        "1-3 a: abcde",
        "1-3 b: cdefg",
        "2-9 c: ccccccccc"
    ]

    def test_part1(self):
        assert part1(self.sample_input) == 2

    def test_part2(self):
        assert part2(self.sample_input) == 1


if __name__ == '__main__':
    unittest.main()
