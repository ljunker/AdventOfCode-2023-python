from math import prod

import networkx as nx

from util import get_input_from_file

graph = nx.Graph()

lines = get_input_from_file("input.txt")

for line in lines:
    v, adj = line.split(": ")
    for a in adj.strip().split(" "):
        graph.add_edge(v, a)

graph.remove_edges_from(nx.minimum_edge_cut(graph))

print(prod([len(c) for c in nx.connected_components(graph)]))
