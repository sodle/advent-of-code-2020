from typing import Dict, List
import numpy as np


def parse_constraints(line: str) -> (str, [range]):
    field, ranges_str = line.split(": ")

    ranges = []
    for range_str in ranges_str.split(" or "):
        a, b = range_str.split("-")
        ranges.append(range(int(a), int(b) + 1))

    return field, ranges


def parse_notes(notes: [str]) -> (Dict[str, List[range]], [int], [[int]]):
    constraints = {}
    nearby_tickets = []

    i = 0
    while True:
        line = notes[i]
        i += 1

        if line == "your ticket:":
            break
        else:
            field, ranges = parse_constraints(line)
            constraints[field] = ranges

    your_ticket = [int(n) for n in notes[i].split(",")]
    i += 2

    while i < len(notes):
        nearby_tickets.append([int(n) for n in notes[i].split(",")])
        i += 1

    return constraints, your_ticket, nearby_tickets


def validate_field(constraints: Dict[str, List[range]], field: int) -> bool:
    for _, field_ranges in constraints.items():
        for field_range in field_ranges:
            if field in field_range:
                return True
    return False


def invalid_ticket_values(constraints: Dict[str, List[range]], ticket: [int]) -> [int]:
    ret = []
    for field in ticket:
        if not validate_field(constraints, field):
            ret.append(field)
    return ret


def candidate_field_names_for_value(constraints: Dict[str, List[range]], value: int) -> {str}:
    ret = set()
    for name, ranges in constraints.items():
        for r in ranges:
            if value in r:
                ret.add(name)
                break
    return ret


def candidate_field_names_for_column(constraints: Dict[str, List[range]], values: [int]) -> {str}:
    return set.intersection(*[candidate_field_names_for_value(constraints, v) for v in values])


def part1(notes: [str]) -> int:
    constraints, _, nearby_tickets = parse_notes(notes)

    invalid = []
    for ticket in nearby_tickets:
        invalid += invalid_ticket_values(constraints, ticket)

    return sum(invalid)


def part2(notes: [str]) -> int:
    constraints, your_ticket, nearby_tickets = parse_notes(notes)

    valid_nearby = [ticket for ticket in nearby_tickets if len(invalid_ticket_values(constraints, ticket)) == 0]

    columns = [[t[i] for t in valid_nearby] for i in range(len(valid_nearby[0]))]
    column_candidates = {i: candidate_field_names_for_column(constraints, v) for i, v in enumerate(columns)}
    column_indices = {}

    while len(column_candidates.keys()):
        new_column_candidates = {}
        newly_determined_columns = set()
        for i, v in column_candidates.items():
            if len(v) == 1:
                print(v)
                col_name = v.pop()
                column_indices[col_name] = i
                newly_determined_columns.add(col_name)
            else:
                new_column_candidates[i] = v
        column_candidates = {i: v.difference(newly_determined_columns) for i, v in new_column_candidates.items()}

    print(column_indices)
    departure_fields = [your_ticket[index] for name, index in column_indices.items() if name.startswith("departure")]
    return np.product(departure_fields)
