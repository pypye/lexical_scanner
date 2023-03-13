from .RegexToNFA import regex_to_nfa
from .AutomataGraph import AutomataGraph

def e_closure_s(data, state, symbol="epsilon"):
    res = [state] if symbol == "epsilon" else []
    for x in data.transitions:
        start = x[0]
        sym = x[1]
        end = x[2]
        if state == start and symbol == sym:
            res.append(end)
            res.extend(e_closure_s(data, end, sym))
    return sorted(list(set(res)))

def e_closure_T(data, states):
    res = []
    for x in states:
        res.extend(e_closure_s(data, x))
    return sorted(list(set(res)))

def move(data, subset, symbol):
    res = []
    for state in subset:
        for x in data.transitions:
            start = x[0]
            sym = x[1]
            end = x[2]
            if state == start and symbol == sym:
                res.append(end)
    return sorted(list(set(res)))

def nfa_to_dfa(data):
    new_transition = []
    Dstates = [e_closure_s(data, data.initial_state)]
    stack = [e_closure_s(data, data.initial_state)]
    while len(stack) > 0:
        T = stack.pop()
        for symbol in data.alphabet:
            U = e_closure_T(data, move(data, T, symbol))
            if len(U) > 0:
                if U not in Dstates:
                    stack.append(U)
                    Dstates.append(U)
                new_transition.append([tuple(T), symbol, tuple(U)])
        
    new_accepting_states = []
    Dstates = [tuple(states) for states in Dstates]
    for states in Dstates:
        if any([y for y in states if y in data.accepting_states]):
            new_accepting_states.append(states)

    new_graph = AutomataGraph({
        "alphabet": data.alphabet,
        "state": Dstates,
        "initial_state": Dstates[0],
        "accepting_states": new_accepting_states,
        "transitions": new_transition
    })

    return new_graph