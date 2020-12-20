import unittest

from . import part1, part2
from . import MessageParser


class Test(unittest.TestCase):
    def test_match_rule_zero(self):
        parser = MessageParser()
        parser.parse_rule("0: 4 1 5")
        parser.parse_rule("1: 2 3 | 3 2")
        parser.parse_rule("2: 4 4 | 5 5")
        parser.parse_rule("3: 4 5 | 5 4")
        parser.parse_rule('4: "a"')
        parser.parse_rule('5: "b"')

        assert len(parser._evaluate_rule("3", "ab")) == 1
        assert parser.matches_rule_zero("ababbb")
        assert parser.matches_rule_zero("abbbab")
        assert not parser.matches_rule_zero("bababa")
        assert not parser.matches_rule_zero("aaabbb")
        assert not parser.matches_rule_zero("aaaabbb")

    def test_match_rule_zero_with_loop(self):
        parser = MessageParser()
        for rule in [
            '42: 9 14 | 10 1',
            '9: 14 27 | 1 26',
            '10: 23 14 | 28 1',
            '1: "a"',
            '11: 42 31 | 42 11 31',
            '5: 1 14 | 15 1',
            '19: 14 1 | 14 14',
            '12: 24 14 | 19 1',
            '16: 15 1 | 14 14',
            '31: 14 17 | 1 13',
            '6: 14 14 | 1 14',
            '2: 1 24 | 14 4',
            '0: 8 11',
            '13: 14 3 | 1 12',
            '15: 1 | 14',
            '17: 14 2 | 1 7',
            '23: 25 1 | 22 14',
            '28: 16 1',
            '4: 1 1',
            '20: 14 14 | 1 15',
            '3: 5 14 | 16 1',
            '27: 1 6 | 14 18',
            '14: "b"',
            '21: 14 1 | 1 14',
            '25: 1 1 | 1 14',
            '22: 14 14',
            '8: 42 | 42 8',
            '26: 14 22 | 1 20',
            '18: 15 15',
            '7: 14 5 | 1 21',
            '24: 14 1',
        ]:
            parser.parse_rule(rule)

        assert parser.matches_rule_zero("bbabbbbaabaabba")
        assert parser.matches_rule_zero("babbbbaabbbbbabbbbbbaabaaabaaa")
        assert parser.matches_rule_zero("aaabbbbbbaaaabaababaabababbabaaabbababababaaa")
        assert parser.matches_rule_zero("bbbbbbbaaaabbbbaaabbabaaa")
        assert parser.matches_rule_zero("bbbababbbbaaaaaaaabbababaaababaabab")
        assert parser.matches_rule_zero("ababaaaaaabaaab")
        assert parser.matches_rule_zero("ababaaaaabbbaba")
        assert parser.matches_rule_zero("baabbaaaabbaaaababbaababb")
        assert parser.matches_rule_zero("abbbbabbbbaaaababbbbbbaaaababb")
        assert parser.matches_rule_zero("aaaaabbaabaaaaababaa")
        assert parser.matches_rule_zero("aaaabbaabbaaaaaaabbbabbbaaabbaabaaa")
        assert parser.matches_rule_zero("aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba")

    def test_part1(self):
        test_input = [
            "0: 4 1 5",
            "1: 2 3 | 3 2",
            "2: 4 4 | 5 5",
            "3: 4 5 | 5 4",
            '4: "a"',
            '5: "b"',
            "ababbb",
            "abbbab",
            "bababa",
            "aaabbb",
            "aaaabbb",
        ]
        assert part1(test_input) == 2

    def test_part2(self):
        test_input = [
            '42: 9 14 | 10 1',
            '9: 14 27 | 1 26',
            '10: 23 14 | 28 1',
            '1: "a"',
            '11: 42 31',
            '5: 1 14 | 15 1',
            '19: 14 1 | 14 14',
            '12: 24 14 | 19 1',
            '16: 15 1 | 14 14',
            '31: 14 17 | 1 13',
            '6: 14 14 | 1 14',
            '2: 1 24 | 14 4',
            '0: 8 11',
            '13: 14 3 | 1 12',
            '15: 1 | 14',
            '17: 14 2 | 1 7',
            '23: 25 1 | 22 14',
            '28: 16 1',
            '4: 1 1',
            '20: 14 14 | 1 15',
            '3: 5 14 | 16 1',
            '27: 1 6 | 14 18',
            '14: "b"',
            '21: 14 1 | 1 14',
            '25: 1 1 | 1 14',
            '22: 14 14',
            '8: 42',
            '26: 14 22 | 1 20',
            '18: 15 15',
            '7: 14 5 | 1 21',
            '24: 14 1',
            'abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa',
            'bbabbbbaabaabba',
            'babbbbaabbbbbabbbbbbaabaaabaaa',
            'aaabbbbbbaaaabaababaabababbabaaabbababababaaa',
            'bbbbbbbaaaabbbbaaabbabaaa',
            'bbbababbbbaaaaaaaabbababaaababaabab',
            'ababaaaaaabaaab',
            'ababaaaaabbbaba',
            'baabbaaaabbaaaababbaababb',
            'abbbbabbbbaaaababbbbbbaaaababb',
            'aaaaabbaabaaaaababaa',
            'aaaabbaaaabbaaa',
            'aaaabbaabbaaaaaaabbbabbbaaabbaabaaa',
            'babaaabbbaaabaababbaabababaaab',
            'aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba'
        ]
        assert part2(test_input) == 12

    if __name__ == '__main__':
        unittest.main()
