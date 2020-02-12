class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist!")


def earliest_ancestor(ancestors, starting_node):
    graph = Graph()
    for pair in ancestors:
        # add vertices
        graph.add_vertex(pair[0])
        graph.add_vertex(pair[1])

        # add edges, but in reverse order
        graph.add_edge(pair[1], pair[0])

    # Now do a BFS
    q = Queue()
    q.enqueue([starting_node])
    path_length = 1
    earliest_ancestor = -1
    while q.size() > 0:
        path = q.dequeue()
        v = path[-1]
        # if (path is equal or longer and the value is smaller)
        # or (if the path is longer)
        if (len(path) >= path_length and v < earliest_ancestor) or (len(path) > path_length):
            earliest_ancestor = v
            path_length = len(path)
        for neighbor in graph.vertices[v]:
            new_path = list(path)
            new_path.append(neighbor)
            q.enqueue(new_path)

    return earliest_ancestor
