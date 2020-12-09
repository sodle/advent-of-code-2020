import unittest

from . import part1, part2


class Test(unittest.TestCase):
    def test_part1(self):
        assert part1([
            35,
            20,
            15,
            25,
            47,
            40,
            62,
            55,
            65,
            95,
            102,
            117,
            150,
            182,
            127,
            219,
            299,
            277,
            309,
            576,
        ], preamble_length=5) == 127

    def test_part2(self):
        assert part2([
            35,
            20,
            15,
            25,
            47,
            40,
            62,
            55,
            65,
            95,
            102,
            117,
            150,
            182,
            127,
            219,
            299,
            277,
            309,
            576,
        ], 127) == 62

    if __name__ == '__main__':
        unittest.main()
