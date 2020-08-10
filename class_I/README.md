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

## ***Traversals***
- **Breadth First Traversal:**
    - Can use a queue: first in, first out
    - Add starting node to queue (initialization step)
    - Dequeue whatever is in front of queue and mark as visited (since we've already been there)
    - Add all of its neighbors to queue
    ```py
    # Init: add starting node to the queue

    # While queue is not empty:
        # Deque node
        # if visited, ignore it
        # else:
            # add all node's neighbors to queue
            # mark node as visited
    ```
- **Breadth First Search:**
    - Will store path to node during traversal (will find the shortest path to target)
    - Can put path into queue, and then visited
    ```py
    def bfs(self, starting_vertex_id, target_vertex_id):
        # Create empty queue and enqueue A PATH TO the starting vertex ID
        # Create a Set to store visited vertices
        # While the queue is not empty...
            # Dequeue the first PATH
            # Grab the last vertex from the PATH
            # If that vertex has not been visited...
                # CHECK IF IT'S THE TARGET
                # IF SO, RETURN PATH
                # Mark it as visited...
                # Then add A PATH TO its neighbors to back of the queue
                # COPY THE PATH
                # APPEND THE NEIGHOR TO THE BACK
    ```


## ***Code Examples***
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
- **Basic Graph II:**
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

    print(g.vertices) #> Output: {1: {2}, 2: {1}}
```
