from typing import List, Dict
from numpy import product


def get_edges(tile: List[str]) -> List[str]:
    return [
        tile[0],
        tile[-1],
        ''.join([row[0] for row in tile]),
        ''.join([row[-1] for row in tile]),
    ]


def count_unique_edges(edge_dict: Dict[int, List[str]]) -> Dict[int, int]:
    all_edges = [edge for _, edges in edge_dict.items() for edge in edges]
    return {idx: len([edge for edge in tile if all_edges.count(edge) + all_edges.count(edge[::-1]) <= 1]) for
            idx, tile in edge_dict.items()}


def part1(input_lines: List[str]) -> int:
    tile_idx = 0
    edge_dict = {}

    tile = []
    for line in input_lines:
        if line.startswith("Tile"):
            if len(tile):
                edge_dict[tile_idx] = get_edges(tile)
                tile = []
            tile_idx = int(line[5:-1])
        else:
            tile.append(line)
    edge_dict[tile_idx] = get_edges(tile)

    unique_edges = count_unique_edges(edge_dict)
    corners = [idx for idx, edges in unique_edges.items() if edges == 2]
    return product(corners)


def part2(input_lines: [str]) -> int:
    pass
