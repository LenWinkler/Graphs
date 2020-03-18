from graph import Graph
from util import Queue

def earliest_ancestor(ancestors, starting_node):

    # build graph

    g = Graph()

    # add vertices
    for ancestor in ancestors:
        g.add_vertex(ancestor[0])
        g.add_vertex(ancestor[1])

    # add edges
    for ancestor in ancestors:
        g.add_edge(ancestor[1], ancestor[0])

    # # traverse graph (BFT)

    # Create a queue
    q = Queue()
    # create a list to hold paths
    paths_list = []
    # Enqueue path the starting node
    q.enqueue([starting_node])
    # While the queue is not empty...
    while q.size() > 0:
        # Dequeue first path
        path = q.dequeue()
        paths_list.append(path)
        # grab last vertex from path
        last_vert = path[-1]
        # Enqueue a path to the parents of its last element
        for parent in g.get_neighbors(last_vert):
            # make a copy of the path and add parent to end of path
            path_copy = path.copy()
            path_copy.append(parent)
            # ENQUEUE THE COPY
            q.enqueue(path_copy)

    # vars for loop
    longest_path = -1
    longest_list = -1
    earliest_ancestor = -1

    # if list length is <= 1 (starting node has no parents), return earliest_ancestor as -1
    if len(paths_list) <=1:
        return earliest_ancestor

    # find longest list(s) and earliest ancestor in paths_list
    for i in range(len(paths_list)):
        if len(paths_list[i]) > longest_path:
            longest_path = len(paths_list[i])
            earliest_ancestor = paths_list[longest_list][-1]

    return earliest_ancestor