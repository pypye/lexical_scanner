from graph.GraphFromVCRegex import build_automata_graph_from_vc_regex
from graph.GraphTraveller import GraphTraveller
from scanner.Scanner import Scanner
import json

graph = build_automata_graph_from_vc_regex()
traveller = GraphTraveller(graph[0], graph[1])


scanner = Scanner("input/in.vc")
token = json.load(open('vc_token/VCTokenDefinition.json'))
state = "0"
current_word = ""

def find_next_state(state, char):
    next_state = None
    if char.isalpha() and char != 'e' and char != 'E':
        next_state = traveller.move(state, "character")
    elif char.isdigit():
        next_state = traveller.move(state, "digit")
    elif char in token.keys():
        next_state = traveller.move(state, token[char])
    else:
        next_state = traveller.move(state, char)
    return next_state

while True:
    if state == None:
        print("Error")
        break

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