from AutomataGraph import AutomataGraph
from ThompsonConstruction import and_rule, or_rule, multiplier_rule, plus_rule

x = AutomataGraph({
    "alphabet": ["a", "b"],
    "state": [0, 1, 4, 3],
    "initial_state": 0,
    "accepting_states": [3],
    "transitions": [
        [0, "a", 1],
        [1, "a", 3],
        [0, "b", 4],
        [4, "b", 3]
    ]
})
y = AutomataGraph({
    "alphabet": ["a", "b"],
    "state": [0, 1, 4, 3],
    "initial_state": 0,
    "accepting_states": [3],
    "transitions": [
        [0, "a", 1],
        [1, "a", 3],
        [0, "b", 4],
        [4, "b", 3]
    ]
})

z = multiplier_rule(x)
print(z)
z.draw()