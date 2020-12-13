import unittest

from . import bezout, part1, part2


class Test(unittest.TestCase):
    def test_bezout(self):
        assert bezout(1785, 546) == (-11, 36)
        assert bezout(3, 20) == (7, -1)
        assert bezout(4, 15) == (4, -1)
        assert bezout(5, 12) == (5, -2)

    def test_part1(self):
        assert part1("7,13,x,x,59,x,31,19", 939) == 295

    def test_part2(self):
        assert part2("7,13,x,x,59,x,31,19") == 1068781
        assert part2("17,x,13,19") == 3417
        assert part2("67,7,59,61") == 754018
        assert part2("67,x,7,59,61") == 779210
        assert part2("67,7,x,59,61") == 1261476
        assert part2("1789,37,47,1889") == 1202161486
        assert part2(
            "41,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,37,x,x,x,x,x,659,x,x,x,x,x,x,x,23,x,x,x,x,13,x,x,x,x,x,19,x,x,x,x,x,x,x,x,x,29,x,937,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,17") == 756261495958122

    if __name__ == '__main__':
        unittest.main()
