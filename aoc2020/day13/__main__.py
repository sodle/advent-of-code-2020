from ..shared import read_input_strings
from . import part1, part2

if __name__ == "__main__":
    [depart_time_str, bus_schedule] = read_input_strings(__file__)
    depart_time = int(depart_time_str)

    print(f"Part 1: {part1(bus_schedule, depart_time)}")
    print(f"Part 2: {part2(bus_schedule)}")
