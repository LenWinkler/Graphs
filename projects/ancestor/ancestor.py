
def earliest_ancestor(ancestors, starting_node):
    # BUILD GRAPH

    # dictionary to store vertices
    vertices = {}
    # add vertices
    for ancestor in ancestors:
        if ancestor[0] not in vertices:
            vertices[ancestor[0]] = set()

        if ancestor[1] not in vertices:
            vertices[ancestor[1]] = set()
        else:
            vertices[ancestor[1]].add(ancestor[0])
    # add edges
    for ancestor in ancestors:
        vertices[ancestor[1]].add(ancestor[0])
    print('graph', vertices)
    print('return empty', vertices[9])
    # function to get edges
    # def get_edges(vertex):

    # # TRAVERSE GRAPH