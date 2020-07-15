import random
from util import Queue

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        # We use the num_users argument to add users to self.users dictionary with the users as the keys and connections as the values
        for user in range(num_users):
            self.add_user(user)

        # Create friendships
        # For each user, we use a random number generator to pick a number between 0 and avg_friendships
        # We connect each user to random number of users
        for user_id in range(1, self.last_id // 2):
            num_of_randos = random.randint(1, avg_friendships)
            # We have a number of friends
            # Now we call add_friendship(single user, N random user id's)
            while len(self.friendships[user_id]) < num_of_randos + 1:
                friend_id = random.randint(user_id, self.last_id)
                self.add_friendship(user_id, friend_id)
        

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME

        qq = Queue()
        qq.enqueue([user_id])

        # We enqueue the user's friends, then we enqueue the friends friends, etc...
        # How do we change the visited dictionary to output:
        # {1: [1], 2: [1, 2], 4: [1, 4], etc...}
        path = []
        while qq.size() > 0:

            path = qq.dequeue()
            user = path[-1]

            if user not in visited:
                visited[user] = path
                # print("Friendships: ", self.friendships[user])
            
                for friend in self.friendships[user]:
                    new_path = list(path)
                    new_path.append(friend)
                    # print("New Path: ", new_path)
                    qq.enqueue(new_path)

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
