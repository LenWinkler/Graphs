"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}  # This is our adjacency list

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph from v1 to v2
        """
        # Check if they exist
        if v1 in self.vertices and v2 in self.vertices:
            # Add the edge
            self.vertices[v1].add(v2)
        else:
            print("ERROR ADDING EDGE: Vertex not found")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            return None
            

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create a q and enqueue starting vertex
        qq = Queue()
        qq.enqueue([starting_vertex])
        # Create a set of traversed vertices
        visited = set()
        # While queue is not empty:
        while qq.size() > 0:
            # dequeue/pop the first vertex
            path = qq.dequeue()
            # if not visited
            if path[-1] not in visited:
                # DO THE THING!!!!!!!
                print(path[-1])
                # mark as visited
                visited.add(path[-1])
                # enqueue all neightbors
                for next_vert in self.get_neighbors(path[-1]):
                    new_path = list(path)
                    new_path.append(next_vert)
                    qq.enqueue(new_path)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create a stack and push starting vertex onto it
        stack = Stack()
        stack.push([starting_vertex])
        # Create a set of traversed vertices
        visited = set()
        # While queue is not empty:
        while stack.size() > 0:
            # dequeue/pop the first vertex
            path = stack.pop()
            # if not visited
            if path[-1] not in visited:
                # DO THE THING!!!!!!!
                print(path[-1])
                # mark as visited
                visited.add(path[-1])
                # push neighbors onto stack
                for next_vert in self.get_neighbors(path[-1]):
                    new_path = list(path)
                    new_path.append(next_vert)
                    stack.push(new_path)

    def dft_recursive(self, starting_vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # add starting_vertex to visited
        visited.add(starting_vertex)
        # print current vertex
        print(starting_vertex)

        # call dft_recursive on every non-visited neighbor
        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
                self.dft_recursive(neighbor)


    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # create queue and enqueue starting_vertex
        queue = Queue()
        queue.enqueue([starting_vertex])
        # create visited set
        visited = set()
        # while queue not not empty
        while queue.size() > 0:
            # dequeue path
            path = queue.dequeue()
            # if last vertex in path = destination_vertex
            if path[-1] == destination_vertex:
                # return path
                return path
            # if vertex not in visited
            if not path[-1] in visited:
                # add it
                visited.add(path[-1])
            # enqueue neighbors
            for neighbor in self.get_neighbors(path[-1]):
                # create copy of path
                new_path = list(path)
                # add neighbor to it
                new_path.append(neighbor)
                # enqueue the new path
                queue.enqueue(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # create stack and push starting vertex onto stack
        stack = Stack()
        stack.push([starting_vertex])
        # create visited set
        visited = set()
        # while stack not empty
        while stack.size() > 0:
            # pop path
            path = stack.pop()
            # if last vertex in path = destination_vertex
            if path[-1] == destination_vertex:
                # return path
                return path
            # if vertex not in visited
            if not path[-1] in visited:
                # add it
                visited.add(path[-1])
            # push neighbors onto stack
            for neighbor in self.get_neighbors(path[-1]):
                # create copy of path
                new_path = list(path)
                # append neighbor
                new_path.append(neighbor)
                # push new_path to stack
                stack.push(new_path)

    def dfs_recursive(self, starting_vertex, destination_vertex, path=list(), visited=set()):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # create copy of path
        new_path = list(path)
        # append/add starting_vertex to new_path and visited
        new_path.append(starting_vertex)
        visited.add(starting_vertex)
        # if last element in path is destination_vertex
        if new_path[-1] == destination_vertex:
            # return path
            return new_path
        
        # call dfs_recursive on non-visited neighbors
        for neighbor in self.get_neighbors(new_path[-1]):
            # check if neighbor in visited
            if not neighbor in visited:
                # call dfs_recursive on neighbor
                returned = self.dfs_recursive(neighbor, destination_vertex, new_path)
                # if return value isn't None, return it
                if returned is not None:
                    return returned 
        


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    # print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    # graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    # graph.dft(1)
    # graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    # print(graph.bfs(1, 6))

    # '''
    # Valid DFS paths:
    #     [1, 2, 4, 6]
    #     [1, 2, 4, 7, 6]
    # '''
    # print(graph.dfs(1, 6))
    # print(graph.dfs_recursive(1, 6))
