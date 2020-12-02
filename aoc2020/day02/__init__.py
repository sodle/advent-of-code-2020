class PasswordEntry(object):
    min_count: int
    max_count: int
    character: chr
    password: str

    def __init__(self, text_entry: str):
        _count_range, _character, self.password = text_entry.split(' ')

        self.min_count, self.max_count = [int(i) for i in _count_range.split('-')]
        self.character = _character[0]

    @property
    def is_valid_part1(self) -> bool:
        matching_chars = [c for c in self.password if c == self.character]
        num_matching = len(matching_chars)
        return self.min_count <= num_matching <= self.max_count

    @property
    def is_valid_part2(self) -> bool:
        # convert from one- to zero- index
        position_a = self.min_count - 1
        position_b = self.max_count - 1

        char_a = self.password[position_a]
        char_b = self.password[position_b]

        return (char_a == self.character and char_b != self.character) or (
                char_b == self.character and char_a != self.character)


def part1(entries: [str]) -> int:
    parsed_entries = [PasswordEntry(e) for e in entries]
    valid_entries = [e for e in parsed_entries if e.is_valid_part1]
    return len(valid_entries)


def part2(entries: [int]) -> int:
    parsed_entries = [PasswordEntry(e) for e in entries]
    valid_entries = [e for e in parsed_entries if e.is_valid_part2]
    return len(valid_entries)
