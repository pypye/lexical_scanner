from vc_token import VCTokenSet
from constructor.AutomataGraphContrustor import automata_graph_contructor
from constructor.ThompsonConstruction import and_rule
from constructor.AutomataGraph import AutomataGraph

def build_automata_graph_from_vc_regex():
    # graph = []
    # for token in VCTokenSet.__dict__:
    #     if '__' not in token:
    #         subgraph = automata_graph_contructor(VCTokenSet.__dict__[token])
    #         graph.append(subgraph)

    # final_graph = graph[0]
    # for i in range(1, len(graph)):
    #     final_graph = or_rule(final_graph, graph[i])

    # final_graph = nfa_to_dfa(final_graph)
    # final_graph = dfa_to_minimise_dfa(final_graph)
    # final_graph.draw()
    automata_graph_contructor(VCTokenSet.FLOATLITERAL).draw()
build_automata_graph_from_vc_regex()


# from constructor.RegexToNFA import regex_to_nfa

# data = regex_to_nfa("((E|e)(plus|minus)?(digit)+)")
# data.draw()