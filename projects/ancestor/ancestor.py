from graph import Graph

def earliest_ancestor(ancestors, starting_node):

    # graph
    g = Graph()
    # set to store visited
    # visited = set()
    # add vertices
    for ancestor in ancestors:
        # if ancestor[0] not in visited:
        g.add_vertex(ancestor[0])
        # visited.add(ancestor[0])
        # if ancestor[1] not in visited:
        g.add_vertex(ancestor[1])
        # visited.add(ancestor[1])
    # add edges
    for ancestor in ancestors:
        print('vertices before', g.vertices)
        g.add_edge(ancestor[1], ancestor[0])
        print('vertices after', g.vertices)

    

    # # TRAVERSE GRAPH (DFT)

    # keep track of furthest ancestor(s)
    

    # create stack
    

    # push starting_node
    

    # while stack is not empty
    



    # # BUILD GRAPH

    # # dictionary to store vertices
    # vertices = {}
    # # add vertices
    # for ancestor in ancestors:
    #     if ancestor[0] not in vertices:
    #         vertices[ancestor[0]] = set()

    #     if ancestor[1] not in vertices:
    #         vertices[ancestor[1]] = set()
    #     else:
    #         vertices[ancestor[1]].add(ancestor[0])
    # # add edges
    # for ancestor in ancestors:
    #     vertices[ancestor[1]].add(ancestor[0])
    # print('graph', vertices)
    # print('return empty', vertices[9])


    # # # TRAVERSE GRAPH (DFT)

    # # keep track of furthest ancestor(s)
    # furthest_ancestor = -1

    # # create stack
    # s = Stack()

    # # push starting_node
    # s.push(starting_node)

    # # while stack is not empty
    # while s.size() > 0:
    #     # pop first node
    #     n = s.pop()
    #     # 