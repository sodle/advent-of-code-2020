import unittest

from . import part1, part2


class Test(unittest.TestCase):
    def test_part1(self):
        assert part1([
            "nop +0",
            "acc +1",
            "jmp +4",
            "acc +3",
            "jmp -3",
            "acc -99",
            "acc +1",
            "jmp -4",
            "acc +6",
        ]) == 5

    def test_part2(self):
        assert part2([
            "nop +0",
            "acc +1",
            "jmp +4",
            "acc +3",
            "jmp -3",
            "acc -99",
            "acc +1",
            "jmp -4",
            "acc +6",
        ]) == 8

    if __name__ == '__main__':
        unittest.main()
