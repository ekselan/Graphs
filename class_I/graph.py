

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

if __name__ == "__main__":
    g = Graph()

    g.add_vertex(1)
    g.add_vertex(2)
    g.add_edge(1,2) #> (1)-->(2) Directed
    g.add_edge(2,1) #> (1)<-->(2) Undirected

    # ^|^|^|^|^|^|^|^|^|^|
    # self.vertices = {
    #     1: set() --> {2}
    #     2: set() --> {1}
    # }