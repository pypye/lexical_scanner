from graph.GraphFromVCRegex import build_automata_graph_from_vc_regex
from graph.GraphTraveller import GraphTraveller
from scanner.Scanner import Scanner
import json

graph = build_automata_graph_from_vc_regex()
traveller = GraphTraveller(graph[0], graph[1])
# graph[0].draw()


scanner = Scanner("input/example_fib.vc")
token = json.load(open('vc_token/VCTokenDefinition.json'))
state = "0"
current_word = ""

def find_next_state(state, char):
    for tk in token.keys():
        if char in token[tk]:
            return traveller.move(state, tk)
    return traveller.move(state, "other")

while True:
    if state == None:
        print("Error")
        break

    word = scanner.peek_word()
    next_state = find_next_state(state, word)
    if traveller.check_end(next_state):
        print(current_word + word, traveller.get_end(next_state))
        current_word = ""
        state = "0"
        if not scanner.seek_word():
            break
        continue

    char = scanner.peek_char()
    next_state = find_next_state(state, char)
    
    if next_state == None and traveller.check_end(state):
        if traveller.get_end(state) != "SPACE":
            print(current_word, traveller.get_end(state))
        current_word = ""
        state = "0"
    else:
        current_word += char
        state = next_state 
        if not scanner.seek_char():
            break

next_state = find_next_state(state, char)
if next_state == None and traveller.check_end(state):
    if traveller.get_end(state) != "SPACE":
        print(current_word, traveller.get_end(state))