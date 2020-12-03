import unittest

from . import part1, part2


class Test(unittest.TestCase):
    sample_input = [1721, 979, 366, 299, 675, 1456]

    def test_part1(self):
        assert part1(self.sample_input) == 514579

    def test_part2(self):
        assert part2(self.sample_input) == 241861950


if __name__ == '__main__':
    unittest.main()
