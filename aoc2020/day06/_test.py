import unittest

from . import count_group, count_union_group, part1, part2


class Test(unittest.TestCase):
    def test_count_group(self):
        assert count_group(['abc']) == 3
        assert count_group(['a', 'b', 'c']) == 3
        assert count_group(['ab', 'ac']) == 3
        assert count_group(['a', 'a', 'a', 'a']) == 1
        assert count_group(['b']) == 1

    def test_count_union_groups(self):
        assert count_union_group(['abc']) == 3
        assert count_union_group(['a', 'b', 'c']) == 0
        assert count_union_group(['ab', 'ac']) == 1
        assert count_union_group(['a', 'a', 'a', 'a']) == 1
        assert count_union_group(['b']) == 1

    def test_part1(self):
        assert part1([
            ['abc'],
            ['a', 'b', 'c'],
            ['ab', 'ac'],
            ['a', 'a', 'a', 'a'],
            ['b']
        ]) == 11

    def test_part2(self):
        assert part2([
            ['abc'],
            ['a', 'b', 'c'],
            ['ab', 'ac'],
            ['a', 'a', 'a', 'a'],
            ['b']
        ]) == 6

    if __name__ == '__main__':
        unittest.main()
