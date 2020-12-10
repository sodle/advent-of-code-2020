import unittest

from . import part1, part2


class Test(unittest.TestCase):
    def test_part1(self):
        assert part1([
            16,
            10,
            15,
            5,
            1,
            11,
            7,
            19,
            6,
            12,
            4,
        ]) == 35

        assert part1([
            28,
            33,
            18,
            42,
            31,
            14,
            46,
            20,
            48,
            47,
            24,
            23,
            49,
            45,
            19,
            38,
            39,
            11,
            1,
            32,
            25,
            35,
            8,
            17,
            7,
            9,
            4,
            2,
            34,
            10,
            3,
        ]) == 220

    def test_part2(self):
        assert part2([
            16,
            10,
            15,
            5,
            1,
            11,
            7,
            19,
            6,
            12,
            4,
        ]) == 8

        assert part2([
            28,
            33,
            18,
            42,
            31,
            14,
            46,
            20,
            48,
            47,
            24,
            23,
            49,
            45,
            19,
            38,
            39,
            11,
            1,
            32,
            25,
            35,
            8,
            17,
            7,
            9,
            4,
            2,
            34,
            10,
            3,
        ]) == 19208

    if __name__ == '__main__':
        unittest.main()
