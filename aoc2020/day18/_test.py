import unittest

from . import part1, part2
from . import evaluate_expression, evaluate_expression_part2


class Test(unittest.TestCase):
    def test_evaluate_expression(self):
        assert evaluate_expression("1 + 2 * 3 + 4 * 5 + 6") == 71
        assert evaluate_expression("1 + (2 * 3) + (4 * (5 + 6))") == 51
        assert evaluate_expression("2 * 3 + (4 * 5)") == 26
        assert evaluate_expression("5 + (8 * 3 + 9 + 3 * 4 * 3)") == 437
        assert evaluate_expression("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))") == 12240
        assert evaluate_expression("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2") == 13632

    def test_evaluate_expression_part2(self):
        assert evaluate_expression_part2("1 + 2 * 3 + 4 * 5 + 6") == 231
        assert evaluate_expression_part2("1 + (2 * 3) + (4 * (5 + 6))") == 51
        assert evaluate_expression_part2("2 * 3 + (4 * 5)") == 46
        assert evaluate_expression_part2("5 + (8 * 3 + 9 + 3 * 4 * 3)") == 1445
        assert evaluate_expression_part2("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))") == 669060
        assert evaluate_expression_part2("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2") == 23340

    def test_part1(self):
        assert part1([
            "2 * 3 + (4 * 5)",
            "5 + (8 * 3 + 9 + 3 * 4 * 3)",
            "5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))",
            "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2",
        ]) == sum([26, 437, 12240, 13632])

    def test_part2(self):
        assert part2([
            "2 * 3 + (4 * 5)",
            "5 + (8 * 3 + 9 + 3 * 4 * 3)",
            "5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))",
            "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2",
        ]) == sum([46, 1445, 669060, 23340])

    if __name__ == '__main__':
        unittest.main()
