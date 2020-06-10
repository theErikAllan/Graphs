from graph import Graph
from util import Queue


def earliest_ancestor(ancestors, starting_node):
    graph = Graph()

    # First, we write a for loop to loop through the ancestors list and create vertices at each of the values
    for family_tuple in ancestors:
        parent = family_tuple[0]
        child = family_tuple[1]
        graph.add_vertex(parent)
        graph.add_vertex(child)

    # Then we write another for loop that goes through the ancestors list again and creates the edges, pointing from the child to the parent
    for family_tuple in ancestors:
        parent = family_tuple[0]
        child = family_tuple[1]
        graph.add_edge(child, parent)

    # Next, we initialize a queue and enqueue the starting node
    qq = Queue()
    qq.enqueue([starting_node])

    # We create a variable for tracking the maximum path length so we know when we have found the ancestor that is farthest away
    current_max_length = 1

    # We initialize earliest ancestor
    earliest_ancestor = -1

    # Here we write a while loop that runs as long as the queue is not empty
    while qq.size() > 0:
        # We dequeue the current path and set vertex to point to the last element in the path
        path = qq.dequeue()
        vertex = path[-1]

        # Then we write an if statement to compare two sets of data to find either:
        # A path that is equal to or longer than the maximum path length we know of and a vertex with a value less than that of the earliest ancestor we know of
        # A path that is greater than the maximum path length we know of
        if (len(path) >= current_max_length and vertex < earliest_ancestor) or (len(path) > current_max_length):
            # If we find one or the other to be true, we mark the current vertex as the earliest ancestor and set the current maximum length to the length of the path we're looking at
            earliest_ancestor = vertex
            current_max_length = len(path)

        # Here we write a for loop to traverse through the neighbors of the vertex we're looking at
        for neighbor in graph.vertices[vertex]:
            # We create a copy of the current path and append each neighbor before enqueuing each new path
            new_path = list(path)
            new_path.append(neighbor)
            qq.enqueue(new_path)

    # Finally, we return the earliest ancestor
    return earliest_ancestor
