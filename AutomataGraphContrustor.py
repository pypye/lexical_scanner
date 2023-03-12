from constructor.RegexToNFA import regex_to_nfa
from constructor.NFAToDFA import nfa_to_dfa
from constructor.DFAToMinimiseDFA import dfa_to_minimise_dfa

def automata_graph_contructor(regex):
    data = regex_to_nfa(regex)
    data = nfa_to_dfa(data)
    data = dfa_to_minimise_dfa(data)
    return data

data = automata_graph_contructor("c(c|n)*")
data.draw()