from room import Room
from player import Player
from world import World
from util import Stack

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
# visited = set()
reverse_compass = {"n":"s", "s":"n", "e":"w", "w":"e"}


# We create a function to leave a trail of breadcrumbs for the player
def breadcrumb_generator(visited=None):
    # We create a base case for an empty set of visited rooms
    if visited is None:
        visited = set()

    # Breadcrumbs will be the trail of breadcrumbs we leave behind to track our movements from the last visited room to the next unvisited room
    breadcrumbs = []

    # We loop through the available exits and move the player through each one
    for room_exit in player.current_room.get_exits():
        # print("Current room: ", player.current_room.id)
        player.travel(room_exit)

        # In the next room, we check to see if the room has been visited
        if player.current_room not in visited:
            # If it has not been visited, we add it to the set
            visited.add(player.current_room)
            # Then we drop a breadcrumb
            breadcrumbs.append(room_exit)
            # And recursively call the function to continue exploring the rooms with the breadcrumbs we have dropped so far
            breadcrumbs = breadcrumbs + breadcrumb_generator(visited)

            # The recursion will end when we reach a room with only one exit, at which point we must backtrack and drop a breadcrumb along the way
            backtrack = reverse_compass[room_exit]
            player.travel(backtrack)
            breadcrumbs.append(backtrack)

        # If the room has been visited, we go back to the previous room
        else:
            # We don't need to leave a breadcrumb here since we have already been to this room
            player.travel(reverse_compass[room_exit])


    # Finally, we output the breadcrumbs
    return breadcrumbs

traversal_path = breadcrumb_generator()

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
