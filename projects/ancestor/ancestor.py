from graph import Graph
from util import Queue

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

    # return -1 if starting_node has no parents
    if not graph.get_neighbors(starting_node):
        return -1
    
    # we'll do a BFT on the graph, starting at starting_node

    # create queue and enqueue starting_node
    queue = Queue()
    queue.enqueue([starting_node])
    # store a list of paths(lists)
    paths = []

    while queue.size() > 0:
        # dequeue path
        path = queue.dequeue()
        # add it to paths list
        paths.append(path)
        # enqueue parents
        for parent in graph.get_neighbors(path[-1]):
            # copy path and add parent
            new_path = path + [parent]
            # enqueue that new path
            queue.enqueue(new_path)

    # at the end, return last element of longest path
    # if multiple paths are tied for longest, return the lesser ancestor(numerically)
    # use for loop to find longest path(s)

    longest_length = 0
    earliest_ancestor = -1

    for path in paths:
        # if path length is greater, we know we have a new earliest ancestor
        if len(path) > longest_length:
            longest_length = len(path)
            earliest_ancestor = path[-1]
        # if equal, we need to pick the ancestor with the lowest numerical value
        if len(path) == longest_length:
            if path[-1] < earliest_ancestor:
                earliest_ancestor = path[-1]


    return earliest_ancestor