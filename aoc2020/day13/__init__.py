import numpy as np


class Bus(object):
    bus_id: int

    def __init__(self, bus_id: int):
        self.bus_id = bus_id

    def first_bus_after(self, timestamp: int) -> int:
        iteration = 1
        while self.bus_id * iteration < timestamp:
            iteration += 1
        return self.bus_id * iteration

    def delay_after(self, timestamp: int):
        undershoot = timestamp % self.bus_id

        if undershoot == 0:
            return 0
        else:
            return self.bus_id - undershoot


def parse_bus_schedule(schedule: str) -> [Bus]:
    buses = schedule.split(",")
    return [Bus(int(bus_id)) for bus_id in buses if bus_id != "x"]


def bezout(a: int, b: int) -> (int, int):
    # Use the Extended Euclidean Algorithm: https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm
    # To find an x, y pair that satisfies Bezout's identity: https://en.wikipedia.org/wiki/B%C3%A9zout%27s_identity
    # For every pair of integers a, b with greatest common divisor d,
    # There exist integers x, y such that ax + by = d

    # Adapted from https://www.geeksforgeeks.org/python-program-for-basic-and-extended-euclidean-algorithms-2/

    # base case
    if a == 0:
        return 0, 1

    x1, y1 = bezout(b % a, a)

    x = y1 - (b // a) * x1
    y = x1

    return x, y


def part1(bus_schedule: str, depart_time: int) -> int:
    buses = parse_bus_schedule(bus_schedule)
    buses.sort(key=lambda b: b.first_bus_after(depart_time))

    bus_time = buses[0].first_bus_after(depart_time)
    wait_time = bus_time - depart_time
    return buses[0].bus_id * wait_time


def part2(bus_schedule: str) -> int:
    # Get (desired time offset, arrival interval) for each defined bus
    buses = [(idx, int(b)) for idx, b in enumerate(bus_schedule.split(",")) if b != "x"]
    print(buses)

    # The Chinese remainder theorem applies: https://en.wikipedia.org/wiki/Chinese_remainder_theorem
    # We will use the buses' arrival intervals as the n-terms
    # And the desired time offsets as the a-terms
    a, n = list(zip(*buses))
    # The theorem defines N as the product of the n-terms
    big_n = np.product(n)
    # And m as N / n.
    # Note the floor division, as the puzzle input numbers are too large for floating point division to be precise.
    m = big_n // n

    # u, v are the Bezout pairs for each n, m.
    # We only need v, the larger one.
    v = [bezout(ni, mi)[1] for ni, mi in zip(n, m)]

    # for every e, n: e is congruent to 1 modulo n
    e = v * m

    # the solution is congruent to x modulo N
    x = sum(a * e)

    # Return the lowest positive number that satisfies the congruency
    return int(big_n - (x % big_n))
