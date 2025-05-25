"""
Question 1
"""

import networkx as nx

def crea_traffic_graph():
    G = nx.DiGraph()

    arete = [
        ("E", "a", 5),
        ("E", "b", 10),
        ("E", "e", 8),
        ("a", "c", 7),
        ("a", "d", 10),
        ("b", "c", 8),
        ("b", "d", 2),
        ("b", "e", 1),
        ("c", "g", 7),
        ("d", "g", 4),
        ("d", "f", 2),
        ("d", "S", 6),
        ("e", "f", 4),
        ("f", "S", 6),
        ("g", "S", 10),
    ]

    for u, v, cap in arete:
        G.add_edge(u, v, capacity=cap)

    return G

def max_vehicule(source="E", sink="S"):
    G = crea_traffic_graph()
    flow_value, flow_dict = nx.maximum_flow(G, source, sink, flow_func=nx.algorithms.flow.edmonds_karp)
    return flow_value, flow_dict
