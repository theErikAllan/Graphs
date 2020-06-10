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
        self.vertices[vertex_id] = set()  # set of edges from this vert
        # a set is like a list except it allows O(1) lookups like a hashtable and it doesn't allow duplicates

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # First we check to see if the vertices we're trying to connect exist
        if v1 in self.vertices and v2 in self.vertices:
            # If they do exist, we add v2 as a neighbor to v1
            self.vertices[v1].add(v2)
        else:
            # If v1 or v2 does not exist, we raise an error
            raise IndexError("Vertex does not exist")

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
        # First we create an empty queue and enqueue the starting vertex
        qq = Queue()
        qq.enqueue(starting_vertex)
        
        # Then we create a set to store the vertices we visit
        visited = set()
        
        # Here we write a while loop that will run as long as the queue is not empty
        while qq.size() > 0:
            # Dequeue the first vertex
            # We dequeue the first vertex and set (v) to it
            v = qq.dequeue()

            # Next we check to see if that vertex has already been visited
            if v not in visited:
                # If if has not been visited, we print it and mark it as visited
                print(v)
                visited.add(v)

                # Then we add all of its neighbors to the back of the queue
                for next_vert in self.get_neighbors(v):
                    qq.enqueue(next_vert)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # First, we create an empty stack and push the starting vertex
        ss = Stack()
        ss.push(starting_vertex)

        # Then we create a set to store the vertices we visit
        visited = set()

        # Here we write a while loop that will run as long as the stack is not empty
        while ss.size() > 0:
            # We pop the node off the top of the stack and set (v) to it
            v = ss.pop()

            # Next we check to see if that vertex has already been visited
            if v not in visited:
                # If it hasn't been visited, we print it out and mark it as visited
                print(v)
                visited.add(v)

                # Lastly, we push all its neighbors on the stack
                for next_vert in self.get_neighbors(v):
                    ss.push(next_vert)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # First, we set our initial condition 
        if visited is None:
            # If no nodes have been visited, we create a set to store the nodes we visit
            visited = set()

        # Then we add the starting vertex to the visited set
        visited.add(starting_vertex)
        print(starting_vertex)

        # Call the function recursively on neighbors not visited
        # Lastly we write a for loop that will recursively call dft_recursive()
        for neighbor in self.vertices[starting_vertex]:
            # For each vertex, we check to see if any of the neighbors have already been visited
            if neighbor not in visited:
                # And if we find a neighbor that has not been visited, we recursively call dft_recursive() and pass it the neighbor and updated visited set
                self.dft_recursive(neighbor, visited)


    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # First, we create an empty queue and enqueue the starting vertex as a list
        qq = Queue()
        qq.enqueue([starting_vertex])

        # Then we create a set to store the vertices we visit
        visited = set()

        # We write a while loop that will run as long as the queue is not empty
        while qq.size() > 0:
            # We dequeue the first vertex and set (v) to it
            v = qq.dequeue()
            # print("This is v: ", v)
            # print("This is v[-1]: ", v[-1])

            # Next we check to see if the vertex we just dequeued has been visited already
            if v[-1] not in visited:
                # If it has not been visited, we check to see if it is the destination we have long been searching for 
                if v[-1] == destination_vertex:
                    # If it is, we return the list of nodes we followed to arrive at said destination
                    return v

                # If it's not the node we are looking for, we mark it as visited
                visited.add(v[-1])

                # Then add all of its neighbors to the back of the queue
                
                # Lastly, we write a for loop that loops through the neighbors of the current vertex
                for next_vert in self.get_neighbors(v[-1]):
                    # For each neighbor, we create a copy of the current path and append the neighbor, allowing us to create multiple paths forward depending on the number of neighbors a vertex has
                    new_v = list(v)
                    new_v.append(next_vert)

                    # Then we enqueue the path to the next neighbor
                    qq.enqueue(new_v)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # First, we create an empty stack and push the starting vertex onto the stack
        ss = Stack()
        ss.push([starting_vertex])

        # Then we create a set to store the vertices we visit
        visited = set()

        # We write a while loop that will run as long as the stack is not empty
        while ss.size() > 0:
            # We pop the node off the top of the stack and set (v) to it
            v = ss.pop()

            # Next we check to see if the last vertex has already been visited
            if v[-1] not in visited:
                # If it hasn't been visited, we check to see if it is the node we're looking 
                if v[-1] == destination_vertex:
                    # If it is, we return the list of nodes we followed to arrive at said destination
                    return v

                # If it's not the node we're looking for, we mark it as visited
                visited.add(v[-1])

                # Lastly, we write a for loop to loop through the neighbors of the vertex we're looking at
                for next_vert in self.get_neighbors(v[-1]):
                    # For each neighbor, we create a copy of the current path and append the neighbor, allowing us to create multiple paths forward depending on the number of neighbors a vertex has
                    new_path = list(v)
                    new_path.append(next_vert)

                    # Then we push to the stack the path to the next neighbor
                    ss.push(new_path)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # First we write a couple if statements for the initial case where there are no visited nodes and therefore no paths
        if visited is None:
            # If nothing has been visited yet, we create an empty set
            visited = set()
        
        if path is None:
            # If there are no stored paths, we create an empty array to initialize path
            path = []


        # Then we add the starting vertex to the list of visited notes and create a copy of the current path plus the starting vertex
        visited.add(starting_vertex)
        new_path = path + [starting_vertex]

        # Then we check to see if the starting vertex is the destination vertex and return the path to said vertex
        if starting_vertex == destination_vertex:
            return new_path

        # Lastly, we write a for loop that loops through the neighbors of the starting vertex
        for neighbor in self.vertices[starting_vertex]:
            # For each neighbor, we check to see if it has been visited already
            if neighbor not in visited:
                # If it has not been visited, we create a variable pointing to the path to said neighbor and then recursively call the function, passing it the neighbor/node we're visiting next, the destination we're looking for, an updated list of visited nodes, and the updated path
                path_to_neighbor = self.dfs_recursive(neighbor, destination_vertex, visited, new_path)

                # Finally, once we have a path to the neighbor, we return it
                if path_to_neighbor:
                    return path_to_neighbor

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
