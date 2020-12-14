import unittest

from . import part1, part2


class Test(unittest.TestCase):
    def test_part1(self):
        test_input = [
            "mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X",
            "mem[8] = 11",
            "mem[7] = 101",
            "mem[8] = 0",
        ]
        assert part1(test_input) == 165

    def test_part2(self):
        test_input = [
            "mask = 000000000000000000000000000000X1001X",
            "mem[42] = 100",
            "mask = 00000000000000000000000000000000X0XX",
            "mem[26] = 1",
        ]
        assert part2(test_input) == 208

    if __name__ == '__main__':
        unittest.main()
