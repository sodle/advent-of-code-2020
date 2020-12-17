import unittest

from . import part1, part2

test_input = [
    ".#.",
    "..#",
    "###",
]


class Test(unittest.TestCase):
    def test_part1(self):
        assert part1(test_input) == 112

    def test_part2(self):
        assert part2(test_input) == 848

    if __name__ == '__main__':
        unittest.main()
