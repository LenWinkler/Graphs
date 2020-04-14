from graph import Graph

def earliest_ancestor(ancestors, starting_node):
    
    # create graph
    # create set to ensure no duplicate vertices
    # loop through input and add vertices
    # loop through again and add edges
    
    # do a BFT on the graph starting at starting_node
    # if starting_node has no parents(neighbors), return -1
    # store a list of paths(lists)
    # at the end, return last element of longest path
    # if multiple paths are tied for longest, return the lesser ancestor(numerically)