from vc_token import VCTokenSet
from constructor.AutomataGraphContrustor import automata_graph_contructor
from constructor.ThompsonConstruction import combine
from constructor.AutomataGraph import AutomataGraph


def build_automata_graph_from_vc_regex():
    graph = []
    graph_end_state_name = {}
    list_token = []
    for token in VCTokenSet.__dict__:
        if '__' not in token:
            subgraph = automata_graph_contructor(VCTokenSet.__dict__[token])
            graph.append(subgraph)
            list_token.append(token)

    final_graph = graph[0]
    
    for state in graph[0].accepting_states:
        graph_end_state_name[state] = list_token[0]

    for i in range(1, len(graph)):
        final_graph = combine(final_graph, graph[i])
        for state in final_graph.accepting_states:
            if state not in graph_end_state_name:
                graph_end_state_name[state] = list_token[i]

    return final_graph, graph_end_state_name

graph = build_automata_graph_from_vc_regex()
graph[0].draw()
print(graph[1])