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
# a = "="
# print(a in token.keys())
# print(token[a])
while True:
    if state == None:
        print("Error")
        break


    char = scanner.peek_char()
    if char.isalpha():
        next_state = traveller.move(state, "character")
    elif char.isdigit():
        next_state = traveller.move(state, "digit")
    elif char in token.keys():
        next_state = traveller.move(state, token[char])
    else:
        next_state = traveller.move(state, char)

    if traveller.check_end(next_state):
        print(current_word, traveller.get_end(next_state))
        current_word = ""
        state = "0"
    else:
        current_word += char
        state = next_state

    if char == "":
        break
        