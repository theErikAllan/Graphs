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
            raise IndexError("Vertex does not exist in graph")

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
        qq = Queue()
        qq.enqueue(starting_vertex)

        visited = set()

        while qq.size() > 0:

            vertex = qq.dequeue()

            if vertex not in visited:
                visited.add(vertex)
                print(vertex)

                for neighbor in self.get_neighbors(vertex):
                    if neighbor not in visited:
                        qq.enqueue(neighbor)


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        ss = Stack()
        ss.push(starting_vertex)

        visited = set()

        while ss.size() > 0:

            vertex = ss.pop()

            if vertex not in visited:
                visited.add(vertex)
                print(vertex)

                for neighbor in self.get_neighbors(vertex):
                    if neighbor not in visited:
                        ss.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # We create a set to track the visited vertices
        if visited is None:
            visited = set()

        # A conditional to check if the starting vertex is in visited
        # Print vertex if not in visited, and add to visited
        if starting_vertex not in visited:
            visited.add(starting_vertex)
            print(starting_vertex)
        # Loop through neighbors and recursively call method on each neighbor
        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
                self.dft_recursive(neighbor, visited)


    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Initialize visited
        visited = set()

        # Initialize Queue
        qq = Queue()
        qq.enqueue([starting_vertex])

        # We write a while loop that runs as long as the queue is not empty
        while qq.size() > 0:

            path = qq.dequeue()

            vertex = path[-1]

            if vertex not in visited:

                if vertex == destination_vertex:
                    return path
                
                visited.add(vertex)
            
                for neighbor in self.get_neighbors(vertex):
                    if neighbor not in visited:
                        # To create a copy of the list we have to use the list() function or else new_path will forever point to path, rather than the list that path is pointing to
                        new_path = list(path)
                        new_path.append(neighbor)
                        qq.enqueue(new_path)



    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        visited = set()

        ss = Stack()
        ss.push([starting_vertex])

        while ss.size() > 0:
            path = ss.pop()

            vertex = path[-1]

            if vertex not in visited:
                if vertex == destination_vertex:
                    return path
                
                visited.add(vertex)

                for neighbor in self.get_neighbors(vertex):
                    if neighbor not in visited:
                        new_path = list(path)
                        new_path.append(neighbor)
                        ss.push(new_path)


    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO

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
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
