import unittest

from . import part1, part2


class Test(unittest.TestCase):
    def test_part1(self):
        assert part1([0, 3, 6]) == 436
        assert part1([1, 3, 2]) == 1
        assert part1([2, 1, 3]) == 10
        assert part1([1, 2, 3]) == 27
        assert part1([2, 3, 1]) == 78
        assert part1([3, 2, 1]) == 438
        assert part1([3, 1, 2]) == 1836

    def test_part2(self):
        assert part2([0, 3, 6]) == 175594
        assert part2([1, 3, 2]) == 2578
        assert part2([2, 1, 3]) == 3544142
        assert part2([1, 2, 3]) == 261214
        assert part2([2, 3, 1]) == 6895259
        assert part2([3, 2, 1]) == 18
        assert part2([3, 1, 2]) == 362

    if __name__ == '__main__':
        unittest.main()
