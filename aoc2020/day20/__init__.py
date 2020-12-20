from typing import List, Dict, NamedTuple
from enum import Enum
from numpy import product


class TileEdge(Enum):
    Left = 'left'
    Right = 'right'
    Top = 'top'
    Bottom = 'bottom'


class Adjacency(NamedTuple):
    other: 'Tile'
    other_edge: TileEdge
    reverse: bool


class Tile(object):
    def __init__(self, tile_id: int, rows: List[str]):
        self.id = tile_id
        self.rows = rows

        self.edges = {
            TileEdge.Top: self.rows[0],
            TileEdge.Bottom: self.rows[-1],
            TileEdge.Left: ''.join([row[0] for row in self.rows]),
            TileEdge.Right: ''.join([row[-1] for row in self.rows]),
        }

        self.neighbors: Dict[TileEdge, Adjacency] = {}


class Board(object):
    def __init__(self):
        self.tiles: List[Tile] = []

    def add_tile(self, tile_id: int, rows: List[str]):
        new_tile = Tile(tile_id, rows)

        for tile in self.tiles:
            for my_side, my_edge in new_tile.edges.items():
                for other_side, other_edge in tile.edges.items():
                    if my_edge == other_edge:
                        tile.neighbors[other_side] = Adjacency(other=new_tile, other_edge=my_side, reverse=False)
                        new_tile.neighbors[my_side] = Adjacency(other=tile, other_edge=other_side, reverse=False)
                    elif my_edge == other_edge[::-1]:
                        tile.neighbors[other_side] = Adjacency(other=new_tile, other_edge=my_side, reverse=True)
                        new_tile.neighbors[my_side] = Adjacency(other=tile, other_edge=other_side, reverse=True)

        self.tiles.append(new_tile)

    @property
    def corner_tiles(self) -> List[Tile]:
        return [tile for tile in self.tiles if len(tile.neighbors) == 2]

    @staticmethod
    def from_lines(input_lines: List[str]) -> 'Board':
        board = Board()

        tile_idx = 0
        tile = []
        for line in input_lines:
            if line.startswith("Tile"):
                if len(tile):
                    board.add_tile(tile_idx, tile)
                    tile = []
                tile_idx = int(line[5:-1])
            else:
                tile.append(line)
        board.add_tile(tile_idx, tile)

        return board


def part1(input_lines: List[str]) -> int:
    board = Board.from_lines(input_lines)
    corners = board.corner_tiles
    return product([corner.id for corner in corners])


def part2(input_lines: [str]) -> int:
    pass
