import unittest

from . import parse_bag_specifier, part1, part2


class Test(unittest.TestCase):
    def test_parse_bag_specifier(self):
        assert parse_bag_specifier("light red bags contain 1 bright white bag, 2 muted yellow bags.") == (
            "light red", [
                ("bright white", 1),
                ("muted yellow", 2),
            ]
        )
        assert parse_bag_specifier("dark orange bags contain 3 bright white bags, 4 muted yellow bags.") == (
            "dark orange", [
                ("bright white", 3),
                ("muted yellow", 4),
            ]
        )
        assert parse_bag_specifier("bright white bags contain 1 shiny gold bag.") == (
            "bright white", [
                ("shiny gold", 1),
            ]
        )
        assert parse_bag_specifier("muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.") == (
            "muted yellow", [
                ("shiny gold", 2),
                ("faded blue", 9),
            ]
        )
        assert parse_bag_specifier("shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.") == (
            "shiny gold", [
                ("dark olive", 1),
                ("vibrant plum", 2),
            ]
        )
        assert parse_bag_specifier("dark olive bags contain 3 faded blue bags, 4 dotted black bags.") == (
            "dark olive", [
                ("faded blue", 3),
                ("dotted black", 4),
            ]
        )
        assert parse_bag_specifier("vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.") == (
            "vibrant plum", [
                ("faded blue", 5),
                ("dotted black", 6),
            ]
        )
        assert parse_bag_specifier("faded blue bags contain no other bags.") == (
            "faded blue", []
        )
        assert parse_bag_specifier("dotted black bags contain no other bags.") == (
            "dotted black", []
        )

    def test_part1(self):
        assert part1([
            "light red bags contain 1 bright white bag, 2 muted yellow bags.",
            "dark orange bags contain 3 bright white bags, 4 muted yellow bags.",
            "bright white bags contain 1 shiny gold bag.",
            "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.",
            "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.",
            "dark olive bags contain 3 faded blue bags, 4 dotted black bags.",
            "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.",
            "faded blue bags contain no other bags.",
            "dotted black bags contain no other bags.",
        ]) == 4

    def test_part2(self):
        assert part2([
            "light red bags contain 1 bright white bag, 2 muted yellow bags.",
            "dark orange bags contain 3 bright white bags, 4 muted yellow bags.",
            "bright white bags contain 1 shiny gold bag.",
            "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.",
            "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.",
            "dark olive bags contain 3 faded blue bags, 4 dotted black bags.",
            "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.",
            "faded blue bags contain no other bags.",
            "dotted black bags contain no other bags.",
        ]) == 32
        assert part2([
            "shiny gold bags contain 2 dark red bags.",
            "dark red bags contain 2 dark orange bags.",
            "dark orange bags contain 2 dark yellow bags.",
            "dark yellow bags contain 2 dark green bags.",
            "dark green bags contain 2 dark blue bags.",
            "dark blue bags contain 2 dark violet bags.",
            "dark violet bags contain no other bags.",
        ]) == 126

    if __name__ == '__main__':
        unittest.main()
