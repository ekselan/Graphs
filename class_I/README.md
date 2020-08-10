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
