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

    def __init__(self):
        self.vertices = {} #> dictionary of verts

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add connection between vertex-v1 and vertex-v2
        (From A to B, from A to C, ...)
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
            # self.vertices[v2].add(v1) > if you knew you wanted
            # undirected

        else:
            raise IndexError("nonexistent vertex")

    def get_neighbors(self, vertex_id):
        """
        Answers the question: What are the neighbors next 
        to this node
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex_id):

        # Create an empty queue
        q = Queue()

        # Add starting vertex id
        q.enqueue(starting_vertex_id)

        # Create set for visited verts
        visited = set()

        # While queue is not empty
        while q.size() > 0:

            # Dequeue a vert
            v = q.dequeue()

            # If not visited
            if v not in visited:

                # Visit it!
                print(v)

                # Mark as visited
                visited.add(v)

                # Add all neighbors to the queue
                for neighbor in self.get_neighbors(v):
                    q.enqueue(neighbor)

if __name__ == "__main__":
    g = Graph()

    g.add_vertex(1)
    g.add_vertex(2)
    g.add_vertex(3)
    g.add_vertex(4)
    g.add_vertex(5)
    g.add_vertex(6)

    g.add_edge(1,2) #> (1)-->(2) Directed
    g.add_edge(1,4)
    g.add_edge(2,3) #> (1)<-->(2) Undirected
    g.add_edge(4,3)
    g.add_edge(3,6)
    g.add_edge(6,5)
    g.add_edge(5,4)

    # ^|^|^|^|^|^|^|^|^|^|
    # self.vertices = {
    #     1: set() --> {2}
    #     2: set() --> {1}
    # }

    print(g.vertices) #> Output: {1: {2}, 2: {1}}

    g.bft(1)
    print("---" * 10)
    g.bft(3)