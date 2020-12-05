import unittest

from . import find_seat, seat_id, part1


class Test(unittest.TestCase):
    def test_find_seat(self):
        assert find_seat("FBFBBFFRLR") == (44, 5)
        assert find_seat("BFFFBBFRRR") == (70, 7)
        assert find_seat("FFFBBBFRRR") == (14, 7)
        assert find_seat("BBFFBBFRLL") == (102, 4)

    def test_seat_id(self):
        assert seat_id("FBFBBFFRLR") == 357
        assert seat_id("BFFFBBFRRR") == 567
        assert seat_id("FFFBBBFRRR") == 119
        assert seat_id("BBFFBBFRLL") == 820

    def test_part1(self):
        assert part1([
            "FBFBBFFRLR",
            "BFFFBBFRRR",
            "FFFBBBFRRR",
            "BBFFBBFRLL"
        ]) == 820


if __name__ == '__main__':
    unittest.main()
