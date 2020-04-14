from graph import Graph

def earliest_ancestor(ancestors, starting_node):
    
    # create graph
    graph = Graph()
    # create set to ensure no duplicate vertices
    vertices = set()
    # loop through input and add vertices
    for pair in ancestors:
        if not pair[0] in vertices:
            graph.add_vertex(pair[0])
        if not pair[1] in vertices:
            graph.add_vertex(pair[1])
    # loop through again and add edges
    for pair in ancestors:
        graph.add_edge(pair[1], pair[0])

    print(graph.vertices)
    
    # do a BFT on the graph starting at starting_node
    # if starting_node has no parents(neighbors), return -1
    # store a list of paths(lists)
    # at the end, return last element of longest path
    # if multiple paths are tied for longest, return the lesser ancestor(numerically)
    
test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

earliest_ancestor(test_ancestors, 1)