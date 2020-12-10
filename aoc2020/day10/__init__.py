import networkx as nx
from numpy.linalg import matrix_power


def graph_joltages(joltages: [int]) -> nx.DiGraph:
    all_joltages = [0, *joltages, max(joltages) + 3]

    g = nx.DiGraph()

    for joltage in sorted(all_joltages):
        g.add_node(joltage)
        for node in g.nodes:
            if joltage - node in [1, 2, 3]:
                g.add_edge(joltage, node)

    return g


def part1(puzzle_input: [int]) -> int:
    g = graph_joltages(puzzle_input)
    path = nx.dag_longest_path(g)

    ones = 0
    threes = 0
    for idx in range(len(path)):
        if idx + 1 < len(path):
            diff = path[idx] - path[idx + 1]
            if diff == 1:
                ones += 1
            elif diff == 3:
                threes += 1

    return ones * threes


def part2(puzzle_input: [int]) -> int:
    g = graph_joltages(puzzle_input)

    # The adjacency matrix (A) shows connectivity between nodes in a graph
    # If the element at row I, column J is 1, then an edge exists from node I to node J
    adjacency = nx.adjacency_matrix(g).todense()

    # Find all paths of all possible lengths from the top node to the bottom
    paths = 0
    for path_length in range(len(g.nodes) + 1):
        # Exponentiating the adjacency matrix (A^n) shows the number of paths of length n between two nodes
        # In this case we want the number of paths from the highest-numbered node (last row)
        # to the lowest (first column)
        paths_of_length = matrix_power(adjacency, path_length)[-1, 0]
        paths += paths_of_length

    return paths
