from graph.GraphFromVCRegex import build_automata_graph_from_vc_regex

graph = build_automata_graph_from_vc_regex()
graph[0].draw()
print(graph[1])