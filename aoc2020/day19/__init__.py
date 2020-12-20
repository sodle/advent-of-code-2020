from typing import List, Dict, NamedTuple
import re

quoted_string = re.compile(r'^"(\w+)"$')


class ParserResult(NamedTuple):
    match: bool
    remainder: str


class MessageParser(object):
    def __init__(self):
        self.rules: Dict[str, List[List[str]]] = {}

    def parse_rule(self, rule_line: str):
        rule_index, rule_value = rule_line.split(": ")
        rule_variants = rule_value.split(" | ")
        self.rules[rule_index] = [rule.split(" ") for rule in rule_variants]

    def _evaluate_rule_variant(self, rule: List[str], target: str) -> List[ParserResult]:
        if len(rule) == 0:
            return []
        elif len(rule) == 1:
            literal_match = quoted_string.match(rule[0])
            if literal_match:
                if len(target) == 0:
                    return []
                elif literal_match.group(1) == target[0]:
                    return [ParserResult(match=True, remainder=target[1:])]
                else:
                    return []
            else:
                return self._evaluate_rule(rule[0], target)
        else:
            first_token_matches = self._evaluate_rule(rule[0], target)
            matches = []
            for match in first_token_matches:
                if match.match:
                    remainder_matches = self._evaluate_rule_variant(rule[1:], match.remainder)
                    for m in remainder_matches:
                        if m.match:
                            matches.append(m)
            return matches

    def _evaluate_rule(self, rule_id: str, target: str) -> List[ParserResult]:
        matches = []
        for variant in self.rules[rule_id]:
            for match in self._evaluate_rule_variant(variant, target):
                if match.match:
                    matches.append(match)
        return matches

    def matches_rule_zero(self, target: str) -> bool:
        for match in self._evaluate_rule("0", target):
            if match.match and len(match.remainder) == 0:
                return True
        return False


def part1(input_lines: [str]) -> int:
    matching_mesages = 0

    parser = MessageParser()
    for line in input_lines:
        if line[0].isdigit():
            parser.parse_rule(line)
        else:
            match = parser.matches_rule_zero(line)
            if match:
                matching_mesages += 1

    return matching_mesages


def part2(input_lines: [str]) -> int:
    matching_mesages = 0

    parser = MessageParser()
    for line in input_lines:
        if line.startswith("8:"):
            actual_line = "8: 42 | 42 8"
        elif line.startswith("11:"):
            actual_line = "11: 42 31 | 42 11 31"
        else:
            actual_line = line

        if actual_line[0].isdigit():
            parser.parse_rule(actual_line)
        else:
            match = parser.matches_rule_zero(actual_line)
            if match:
                matching_mesages += 1

    return matching_mesages
