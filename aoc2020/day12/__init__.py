import re, math

nav_regex = re.compile(r"^([NSEWLRF])(\d+)$")


def parse_nav(instruction: str) -> (str, int):
    direction, distance_str = nav_regex.match(instruction).groups()
    return direction, int(distance_str)


def part1(puzzle_input: [[str]]) -> int:
    heading = 0  # straight eastwards, on the unit circle
    lon = 0
    lat = 0

    print(f"hdg={heading} lon={lon} lat={lat}")
    for line in puzzle_input:
        direction, distance = parse_nav(line)
        if direction == "N":
            lat += distance
        elif direction == "S":
            lat -= distance
        elif direction == "E":
            lon += distance
        elif direction == "W":
            lon -= distance
        elif direction == "L":
            heading += distance  # this seems backwards but trust me the unit circle opens counterclockwise
        elif direction == "R":
            heading -= distance
        elif direction == "F":
            heading_rad = math.radians(heading)
            lon += distance * math.cos(heading_rad)
            lat += distance * math.sin(heading_rad)

        print(f"hdg={heading} lon={lon} lat={lat}")

    return abs(lon) + abs(lat)


def part2(puzzle_input: [[str]]) -> int:
    waypoint_lon = 10
    waypoint_lat = 1

    ship_lon = 0
    ship_lat = 0

    print(f"ship=({ship_lon}E, {ship_lat}N) waypoint=({waypoint_lon}E, {waypoint_lat}N)")
    for line in puzzle_input:
        dx = waypoint_lon - ship_lon
        dy = waypoint_lat - ship_lat

        direction, distance = parse_nav(line)

        if direction == "N":
            waypoint_lat += distance
        elif direction == "S":
            waypoint_lat -= distance
        elif direction == "E":
            waypoint_lon += distance
        elif direction == "W":
            waypoint_lon -= distance
        elif direction in "LR":
            move_rad = math.radians(distance if direction == "L" else -distance)

            # Two-dimensional rotation matrix: https://en.wikipedia.org/wiki/Rotation_%28mathematics%29#Two_dimensions
            new_dx = dx * math.cos(move_rad) - dy * math.sin(move_rad)
            new_dy = dx * math.sin(move_rad) + dy * math.cos(move_rad)

            waypoint_lon = ship_lon + new_dx
            waypoint_lat = ship_lat + new_dy
        elif direction == "F":
            ship_lon += distance * dx
            ship_lat += distance * dy

            waypoint_lon += distance * dx
            waypoint_lat += distance * dy

        print(f"ship=({ship_lon}E, {ship_lat}N) waypoint=({waypoint_lon}E, {waypoint_lat}N)")

    return abs(ship_lon) + abs(ship_lat)
