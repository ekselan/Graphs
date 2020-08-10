# Graphs
Class I Notes

## ***Terminology***
- **Nodes/Vertexes/Vertices**: the data components of the graph
- **Edges:** the connections between nodes
- **Directed vs Undirected:**
    - **Directed** - have one-way edges
    - **Undirected** - all edges are two-way
- **Cyclic vs Acyclic:**
    - **Cyclic**: There is at least one "loop"
    - **Acyclic**: there are no loops at all
- **Dense vs Sparse:**
    - **Dense** - high ratio of edges to nodes, nodes are connected to many other nodes
    - **Sparse** - nodes are connected to few other nodes
- **Weighted vs Unweighted:**
    - **Weighted** - edges have associated weights
    - **Unweighted** - edges do not, are all the same weight

## ***Graph Representations***
- **Adjacency Matrix:**
```py
#   A   B   C   D

# A f   T   T   T

# B f   f   f   T

# C f   f   f   f

# D f   f   f   f
```

## ****Code Examples***
- **Basic Graph Implementation:**
```py
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
        self.vertices[v1].add(v2)

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
```