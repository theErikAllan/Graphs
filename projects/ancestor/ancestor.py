from graph import Graph
from util import Stack

def earliest_ancestor(ancestors, starting_node):
    # Function takes in the graph of ancestors and the starting node
    # Returns the earliest known ancestor, the one farthest from the starting node
    # If there is more than one "earliest" ancestor, return the one with the lower numeric ID
    # If starting node has no parents, return -1
    gg = Graph()

    # We want to take the ancestors parameter and turn it into a traversable graph
    for family_tuple in ancestors:
        child = family_tuple[1]
        parent = family_tuple[0]
        gg.add_vertex(child)
        gg.add_vertex(parent)
    
    for family_tuple in ancestors:
        child = family_tuple[1]
        parent = family_tuple[0]
        gg.add_edge(child, parent)
    
    # Since we are trying to find the farthest node from where we're starting, we will initialize a Stack
    ss = Stack()
    ss.push([starting_node])
    path = []
    earliest_ancestor = -1
    current_max_length = 1

    # We use a while loop to traverse the graph until the stack is empty
    while ss.size() > 0:
        # We pop the top off the stack and set path to point to it
        path = ss.pop()
        # We use a variable to point to the last node in the path
        current_node = path[-1]

        # We use a conditional to update the earliest ancestor and maximum path length as we traverse the graph
        # We are looking for the nodes that are furthest away and in the event two nodes are the same distance away, we are looking for the one with a lesser value
        if len(path) > current_max_length or (len(path) >= current_max_length and current_node < earliest_ancestor):
            current_max_length = len(path)
            earliest_ancestor = current_node
        
        # We loop through the parents of the current node, update the path to each parent, and push those new paths to the stack
        for next_parent in gg.vertices[current_node]:
            new_path = list(path)
            new_path.append(next_parent)
            ss.push(new_path)
    
    # Lastly, we return the earliest ancestor
    return earliest_ancestor