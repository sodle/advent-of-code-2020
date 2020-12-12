import unittest

from . import parse_nav, part1, part2

test_input = [
    "F10",
    "N3",
    "F7",
    "R90",
    "F11",
]


class Test(unittest.TestCase):
    def test_parse_nav(self):
        assert [parse_nav(instruction) for instruction in test_input] == [
            ("F", 10),
            ("N", 3),
            ("F", 7),
            ("R", 90),
            ("F", 11),
        ]

    def test_part1(self):
        assert part1(test_input) == 25

    def test_part2(self):
        assert part2(test_input) == 286

    if __name__ == '__main__':
        unittest.main()
