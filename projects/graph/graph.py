"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        # Using Adjaceny List to set up a new vertex
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # first check to make sure both vertices exist before connecting them
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        # returns the Adjacency list value array for the key (vertex_id) passed
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # look into using a python deck
        # Create an empty queue
        q = Queue()
        # engueue the the starting vertex
        q.enqueue(starting_vertex)
        # create a set to store visited vertices
        visited = set()
        # while the queue is not empty...
        while q.size() > 0:
            # dequeue the first vertex in the queue
            v = q.dequeue()
            # if vertex has not already been visited
            if v not in visited:
                print(v)
                # add to the visited vertices set
                visited.add(v)
                # get the neighbors of the vertex and add to the queue
                for next_v in self.get_neighbors(v):
                    q.enqueue(next_v)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        s = Stack()
        s.push(starting_vertex)
        visited = set()
        while s.size() > 0:
            v = s.pop()
            if v not in visited:
                print(v)
                visited.add(v)
                for next_v in self.get_neighbors(v):
                    s.push(next_v)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        visited.add(starting_vertex)
        print(starting_vertex)
        for neighbor in self.vertices[starting_vertex]:
            if neighbor not in visited:
                self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create an empty queue
        q = Queue()
        # engueue the PATH of the starting vertex (i.e. store in an array)
        q.enqueue([starting_vertex])
        # create a set to store the visited vertices
        visited = set()  
        # while the queue is not empty
        while q.size() > 0:
            # DEQUEUE the first PATH
            path = q.dequeue()
            # grab the last vertex from the PATH
            v = path[-1]
            # if that vertex has not been visited...
            if v not in visited:
                # check if it is the target
                if v == destination_vertex:
                    # if so, return the PATH
                    return path
                # mark it as visited
                visited.add(v)
                # then add a path to each neighbor to the end of the queue
                for next_vert in self.get_neighbors(v):
                    # copy the path
                    new_path = list(path)
                    # append the neighbor to the end of the PATH
                    new_path.append(next_vert)
                    # load PATH with neighbor added to the search queue
                    q.enqueue(new_path)
        return None

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()
        s.push([starting_vertex]) # push starting vertex as an array item
        visited = set()  # keeps track of already visited nodes
        while s.size() > 0:
            path = s.pop()  # contains array of path searched
            # print('path = ', path)
            v = path[-1]  # get last node added to the search path
            # print('v = ', v)
            if v not in visited:  # if it has not already been searched
                if v == destination_vertex:  # check if it is our search value
                    return path  # if so, return the search path array
                visited.add(v)  # else add the node to the visited nodes set
                # for each of the node's neighbors
                for next_vert in self.get_neighbors(v):
                    # set up a new path by first copying the existing path
                    # of how we got to this particular vertex
                    new_path = list(path) 
                    # print('new_path = ', new_path)
                    # add v's neighbors to new path array
                    new_path.append(next_vert)
                    # print('new_path after append = ', new_path)
                    # load new path array into search queue to be searched
                    s.push(new_path)
                    # print('************************************')
        return None

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # if first call to the method, setup visited set and path array
        if visited is None:
            visited = set()
        if path is None:
            path = []

        # add each noded visted
        visited.add(starting_vertex)  
        # add each node visited to the path
        path = path + [starting_vertex]  
        # check node for destination_vertex
        if starting_vertex == destination_vertex:  
            return path
        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
                # recusrse on each neighbor visited
                new_path = self.dfs_recursive(
                    neighbor, destination_vertex, visited, path)
                if new_path:
                    return new_path
        return None


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

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    # print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
