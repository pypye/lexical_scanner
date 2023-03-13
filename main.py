from vc_token import VCTokenSet
from constructor.AutomataGraphContrustor import automata_graph_contructor
from constructor.ThompsonConstruction import combine
from constructor.AutomataGraph import AutomataGraph


def build_automata_graph_from_vc_regex():
    graph = []
    for token in VCTokenSet.__dict__:
        if '__' not in token:
            subgraph = automata_graph_contructor(VCTokenSet.__dict__[token])
            graph.append(subgraph)

    final_graph = graph[0]
    for i in range(1, len(graph)):
        final_graph = combine(final_graph, graph[i])


    return final_graph

graph = build_automata_graph_from_vc_regex()