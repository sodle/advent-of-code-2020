import re

import networkx as nx
from networkx.exception import NetworkXNoPath

content_specifier_regex = re.compile(r'(\d+) ([\w\s]+) bags?\.?')


def parse_bag_specifier(bag_specifier: str) -> (str, [(str, int)]):
    color, contents_string = bag_specifier.split(" bags contain ")

    contents = []
    content_specifiers = contents_string.split(", ")
    for content_specifier in content_specifiers:
        match = content_specifier_regex.match(content_specifier)
        if match:
            content_count, content_color = match.groups()
            contents.append((content_color, int(content_count)))

    return color, contents


def parse_bag_graph(bag_specifiers: [str]) -> nx.DiGraph:
    g = nx.DiGraph()

    for specifier in bag_specifiers:
        color, contents = parse_bag_specifier(specifier)
        for inner_bag in contents:
            inner_color, inner_count = inner_bag
            g.add_edge(color, inner_color, count=inner_count)

    return g


def get_bag_size(g: nx.DiGraph, color: str) -> int:
    size = 1
    for color, attr in g[color].items():
        size += get_bag_size(g, color) * attr['count']
    return size


def part1(bag_specifiers: [str]) -> int:
    g = parse_bag_graph(bag_specifiers)

    ancestors = []
    for bag_color in g.nodes:
        try:
            paths = nx.all_shortest_paths(g, bag_color, 'shiny gold')
            for path in paths:
                if len(path) > 1:
                    ancestors.append(bag_color)
                    break
        except NetworkXNoPath:
            pass

    return len(ancestors)


def part2(bag_specifiers: [str]) -> int:
    g = parse_bag_graph(bag_specifiers)
    return get_bag_size(g, 'shiny gold') - 1
