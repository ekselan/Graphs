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
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        
        else:
            raise IndexError("nonexistent vertex")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create an empty queue
        q = Queue()

        # Add starting vertex id
        q.enqueue(starting_vertex)

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

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create an empty stack
        s = Stack()

        # Add starting vertex id
        s.push(starting_vertex)

        # Create set for visited verts
        visited = set()

        # While stack is not empty
        while s.size() > 0:

            # Pop a vert
            v = s.pop()

            # If not visited
            if v not in visited:
                
                # Visit it!
                print(v)

                # Mark as visited
                visited.add(v)

                # Add all neighbors to stack
                for neighbor in self.get_neighbors(v):
                    s.push(neighbor)

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
        # Create empty queue and enqueue a path to starting vertex
        q = Queue()

        # Create a Set to store visited vertices
        visited = set()

        # While the queue is not empty...
        while q.size() > 0:

            # Dequeue the first PATH
            v = q.dequeue()
            print(v)

            # Grab the last vertex from the PATH
            last_v = v[-1]

            # If that vertex has not been visited...
            if last_v in visited:
                continue

            else:

                # Mark it as visited...
                visited.add(last_v)

            # Add A PATH TO its neighbors to back of the queue
            # COPY THE PATH
            # APPEND THE NEIGHOR TO THE BACK
            for neighbor in self.get_neighbors(last_vertex):
                next_path = v[:]
                next_path.append(neighbor)
                
                # CHECK IF IT'S THE TARGET
                if neighbor == destination_vertex:
                    # IF SO, RETURN PATH
                    return next_path

                else:
                    q.enqueue(next_path)
                
                
    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        pass  # TODO

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        
        if visited is None:
            visited = set()

        if path is None:
            path = []

        visited.add(starting_vertex)

        # path = path + [starting_vertex] #> one line for two lines below

        path = list(path) #> make a copy
        path.append(starting_vertex)

        if starting_vertex == destination_vertex:
            return path

        for neighbor in self.get_neighbors(starting_vertex):

            if neighbor not in visited:
                new_path = self.dfs_recursive(neighbor, destination_vertex, visited, path)
                if new_path:
                    return new_path

        return None

if __name__ == "__main__":
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
    print("VERTICES")
    print(graph.vertices)

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
    print("BREADTH FIRST TRAVERSAL")
    graph.bft(1)
    print("---" * 10)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print("DEPTH FIRST TRAVERSAL")
    graph.dft(1)
    print("---" * 10)
    print("DEPTH FIRST TRAVERSAL - RECURSIVE")
    graph.dft_recursive(1)
    print("---" * 10)

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
    print("DEPTH FIRST SEARCH - RECURSIVE")
    print(graph.dfs_recursive(1, 6))
    print("---" * 10)