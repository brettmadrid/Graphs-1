'''
Write a function that takes a 2D binary array
and returns the number of 1 islands.
An island consists of 1's that are connected to the
north, south, east, or west.
'''

islands = [
    [0, 1, 0, 1, 0],
    [1, 1, 0, 1, 1],
    [0, 0, 1, 0, 0],
    [1, 0, 1, 0, 0],
    [1, 1, 0, 0, 0]
]

big_islands = [[1, 0, 0, 1, 1, 0, 1, 1, 0, 1],
               [0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
               [0, 1, 1, 1, 0, 0, 0, 1, 0, 1],
               [0, 0, 1, 0, 0, 1, 0, 0, 1, 1],
               [0, 0, 1, 1, 0, 1, 0, 1, 1, 0],
               [0, 1, 0, 1, 1, 1, 0, 1, 0, 0],
               [0, 0, 1, 0, 0, 1, 1, 0, 0, 0],
               [1, 0, 1, 1, 0, 0, 0, 1, 1, 0],
               [0, 1, 1, 0, 0, 0, 1, 1, 0, 0],
               [0, 0, 1, 1, 0, 1, 0, 0, 1, 0]]


class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self, value):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


def get_neighbors(vertex, graph_matrix):
    x = vertex[0]
    y = vertex[1]
    neighbors = []
    # check north
    if y > 0 and graph_matrix[y-1][x] == 1:
        neighbors.append((x, y-1))
    # check south
    if y < len(graph_matrix) - 1 and graph_matrix[y+1][x] == 1:
        neighbors.append((x, y+1))
    # check east
    if x < len(graph_matrix[0]) - 1 and graph_matrix[y][x+1] == 1:
        neighbors.append((x+1, y))
    # check west
    if x > 0 and graph_matrix[y][x-1] == 1:
        neighbors.append((x-1, y))
    return neighbors


def bft(x, y, matrix, visited):
    # Create an empty queue
    q = Queue()
    # engueue the the starting vertex tuple
    q.enqueue((x, y))
    # while the queue is not empty...
    while q.size() > 0:
        # dequeue the first vertex in the queue
        v = q.dequeue((x, y))
        x = v[0]
        y = v[1]
        # if vertex has not already been visited
        if not visited[y][x]:
            visited[y][x] = True
            # get the neighbors of the vertex and add to the queue
            for neighbor in get_neighbors((x, y), matrix):
                q.enqueue(neighbor)
    return visited


def island_counter(matrix):  # should return 4
    # loop through the islands
    # count how many times a bfs occur
    # create a visited matrix
    visited = []
    for i in range(len(matrix)):
        visited.append([False] * len(matrix[0]))
    # inititalize counter to zero
    counter = 0
    # walk through each cell in the original matrix
    # for each value in the inner arrays
    for x in range(len(matrix[0])):
        # for the total number of array rows in the matrix
        for y in range(len(matrix)):
            # if it has not been visited
            # y is the row and x is the value in the row
            if not visited[y][x]:
                # if it equals a 1
                if matrix[y][x] == 1:
                    # do a bft and mark each one as visited
                    visited = bft(x, y, matrix, visited)
                    # Increment counter by one
                    counter += 1
    return counter


print(island_counter(big_islands))
