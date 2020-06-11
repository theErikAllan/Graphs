import random
import time
from util import Queue

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0  # automatically increment the ID when assigning the new user
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        # We check to see if the user_id being passed in matches the friend_id we're trying to add, and if they match, we return a warning message because you can't "technically" be friends with yourself
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        
        # Else, we check to see:
        # - if the friend_id we're trying to add is in the friendships dictionary for the user_id in question
        # - or if the user_id passed in is in the friendships dictionary for the friend_id
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            # If either is true, we print a warning that a friendship between the two already exists and so cannot be duplicated
            print("WARNING: Friendship already exists")

        # If we make it past both conditional statements, the potential friendship is valid and we can create the connection by adding the user_id and friend_id to one another's friendships
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        # We increment last_id to assign the new user
        self.last_id += 1  
        # Then we create a key:value pair with last_id as the key and the user's name as the value
        self.users[self.last_id] = User(name)
        # Lastly, we create a key:value pair in self.friendships with the last_id as the key and an empty set as the value so we can add the user's friendships as we go
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # First we write a for loop that loops through the number of users being added
        for i in range(0, num_users):
            # For each value of (i), we create a user by assigning it the i value
            self.add_user(f'User {i+1}')

        # We create an empty array to store the potential friendships we'll be adding
        potential_friendships = []

        # We write a for loop to go through the users
        for user in self.users:
            # Then we write another for loop that loops through a range from (user+1) to (last_id+1), which will find all possible combinations of users and friends
            for friend in range(user + 1, self.last_id + 1):
                # We then append the combination of user and friend to the list of potential friendships
                potential_friendships.append((user, friend))

        # We use random.shuffle to create chaos from the orderly list of potential friendships we just built
        random.shuffle(potential_friendships)

        # Lastly, we write a for loop to loop through a range from 0 to the total number of friendships based on the number of users we have multiplied by the average number of friendships, and then divide by two to take into account that a friendship goes both ways, so we don't need to count (1, 2) and (2, 1) as two friendships
        for i in range(num_users * avg_friendships // 2):
            friendship = potential_friendships[i]
            self.add_friendship(friendship[0], friendship[1])


    def populate_graph_2(self, num_users, avg_friendships):
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        collisions = 0

        # Add users
        for i in range(0, num_users):
            self.add_user(f'User {i}')
        
        target_friendships = (num_users * avg_friendships) // 2
        total_friendships = 0

        while total_friendships < target_friendships:
            user_id = random.randint(1, self.last_id)
            friend_id = random.randint(1, self.last_id)
            if self.add_friendship(user_id, friend_id):
                total_friendships += 1
            else:
                collisions += 1
        
        print(f'Collisions: {collisions}')

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME

        # Since it's looking for the shortest friendship path, we will use breadth first traversal

        # With a given user_id, we will do a breadth first traversal and return the path to each friend

        # First, we create a queue
        qq = Queue()
        # And enqueue user_id as a list so we can update it as we go
        qq.enqueue([user_id])

        # We write a while loop that will run until the queue is empty
        while qq.size() > 0:
            # We dequeue the path and set vertex to the last node in the path
            path = qq.dequeue()
            vertex = path[-1]

            # Then we check to see if the vertex has been visited
            if vertex not in visited:
                # If it has not been visited, we set the value of the vertex key to be the path to said vertex
                visited[vertex] = path

                # Then we use a for loop to go through all the neighbors of the vertex in question
                for neighbor in self.friendships[vertex]:
                    # For each neighbor, we create a new path and append the neighbor to it before adding the new path to the queue
                    new_path = path
                    new_path.append(neighbor)
                    qq.enqueue(new_path)
                    # As an alternative, we can use
                    # qq.enqueue(path + [neighbor])
                    # to enqueue a new path without creating a variable first

        # Lastly, we return the dictionary of visited
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    start_time = time.time()
    sg.populate_graph(100, 3)
    end_time = time.time()
    print("These are friendships:")
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print("These are connections:")
    print(connections)

    # for i in range(1, 100):
    #     connections = sg.get_all_social_paths(i)

    #     users_in_ext_network = len(connections) - 1
    #     total_users = len(sg.users)

    #     percentage = users_in_ext_network / total_users * 100

    #     print(f'Percentage: {percentage:.2f}')