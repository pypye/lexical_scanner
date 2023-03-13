from graphviz import Digraph

class AutomataGraph():
    def __init__(self, data):
        self.alphabet = data["alphabet"]
        self.state = data["state"]
        self.initial_state = data["initial_state"]
        self.accepting_states = data["accepting_states"]
        self.transitions = data["transitions"]
        self.normalize_index()

        
    def normalize_index(self, start_index=0):
        normalized_dict = {}
        for i, state in enumerate(self.state):
            normalized_dict[state] = i + start_index

        self.state = [str(normalized_dict[state]) for state in self.state]
        self.initial_state = str(normalized_dict[self.initial_state])
        self.accepting_states = [str(normalized_dict[state]) for state in self.accepting_states]
        self.transitions = [[str(normalized_dict[transition[0]]), str(transition[1]), str(normalized_dict[transition[2]])] for transition in self.transitions]

    def __str__(self):
        ans = "Alphabet: " + str(self.alphabet) + "\n"
        ans += "State: " + str(self.state) + "\n"
        ans += "Initial State: " + str(self.initial_state) + "\n"
        ans += "Accepting States: " + str(self.accepting_states) + "\n"
        ans += "Transitions: " + str(self.transitions) + "\n"
        return ans
    
    def draw(self):
        self.graph = Digraph()
        for x in self.state:
            if (x not in self.accepting_states):
                self.graph.attr('node', shape='circle')
                self.graph.node(x)
            else:
                self.graph.attr('node', shape='doublecircle')
                self.graph.node(x)

        self.graph.attr('node', shape='none')
        self.graph.node('')
        self.graph.edge('', self.initial_state)
        for x in self.transitions:
            self.graph.edge(x[0], x[2], label=('ε', x[1])[x[1] != 'epsilon'])
        
        self.graph.render('nfa', view=True)
 