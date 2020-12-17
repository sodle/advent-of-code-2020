from typing import Dict


class PocketDimension(object):
    def __init__(self, initial_state: [str]):
        self.cubes: Dict[(int, int, int), bool] = {}

        for y, row in enumerate(initial_state):
            for x, col in enumerate(row):
                self.cubes[x, y, 0] = col == "#"

    def expansion_indices(self) -> [(int, int, int)]:
        for index in self.cubes:
            for neighbor in PocketDimension.neighbors_of(*index):
                if neighbor not in self.cubes:
                    yield neighbor

    def update_square(self, x: int, y: int, z: int) -> bool:
        active_neighbors = 0
        current_state = self.cubes[x, y, z] if (x, y, z) in self.cubes else False

        for neighbor in PocketDimension.neighbors_of(x, y, z):
            if neighbor in self.cubes and self.cubes[neighbor] is True:
                active_neighbors += 1

        if current_state is True:
            return active_neighbors in [2, 3]
        else:
            return active_neighbors == 3

    def tick(self):
        all_indices = list(self.cubes.keys()) + list(self.expansion_indices())
        new_cubes = {index: self.update_square(*index) for index in all_indices}
        self.cubes = new_cubes

    @property
    def num_active_cubes(self) -> int:
        return len([i for i in self.cubes if self.cubes[i] is True])

    @staticmethod
    def neighbors_of(x: int, y: int, z: int) -> [(int, int, int)]:
        for nx in [x - 1, x, x + 1]:
            for ny in [y - 1, y, y + 1]:
                for nz in [z - 1, z, z + 1]:
                    coord = (nx, ny, nz)
                    if coord != (x, y, z):
                        yield coord


class PocketHyperDimension(object):
    def __init__(self, initial_state: [str]):
        self.cubes: Dict[(int, int, int, int), bool] = {}

        for y, row in enumerate(initial_state):
            for x, col in enumerate(row):
                self.cubes[x, y, 0, 0] = col == "#"

    def expansion_indices(self) -> [(int, int, int, int)]:
        for index in self.cubes:
            for neighbor in PocketHyperDimension.neighbors_of(*index):
                if neighbor not in self.cubes:
                    yield neighbor

    def update_square(self, x: int, y: int, z: int, w: int) -> bool:
        active_neighbors = 0
        current_state = self.cubes[x, y, z, w] if (x, y, z, w) in self.cubes else False

        for neighbor in PocketHyperDimension.neighbors_of(x, y, z, w):
            if neighbor in self.cubes and self.cubes[neighbor] is True:
                active_neighbors += 1

        if current_state is True:
            return active_neighbors in [2, 3]
        else:
            return active_neighbors == 3

    def tick(self):
        all_indices = list(self.cubes.keys()) + list(self.expansion_indices())
        new_cubes = {index: self.update_square(*index) for index in all_indices}
        self.cubes = new_cubes

    @property
    def num_active_cubes(self) -> int:
        return len([i for i in self.cubes if self.cubes[i] is True])

    @staticmethod
    def neighbors_of(x: int, y: int, z: int, w: int) -> [(int, int, int, int)]:
        for nx in [x - 1, x, x + 1]:
            for ny in [y - 1, y, y + 1]:
                for nz in [z - 1, z, z + 1]:
                    for nw in [w - 1, w, w + 1]:
                        coord = (nx, ny, nz, nw)
                        if coord != (x, y, z, w):
                            yield coord


def part1(initial_state: [str]) -> int:
    dimension = PocketDimension(initial_state)

    for _ in range(6):
        dimension.tick()

    return dimension.num_active_cubes


def part2(initial_state: [str]) -> int:
    dimension = PocketHyperDimension(initial_state)

    for _ in range(6):
        dimension.tick()

    return dimension.num_active_cubes
