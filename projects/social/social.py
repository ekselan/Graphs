import random

# Bring in queue class for use with SocialGraph


class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


class User:
    def __init__(self, name):
        self.name = name


class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def __repr__(self):
        return f"User({repr(self.name)})"

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        # > change add_friendships to T/F for use with pup_graph2
        if user_id == friend_id:
            # print("WARNING: You cannot be friends with yourself")
            return False
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            # print("WARNING: Friendship already exists")
            return False
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

        return True

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def reset(self):
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.reset()

        # Add users
        for i in range(num_users):
            self.add_user(f"User {i}")

        # Create friendships
        possible_friendships = []

        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append((user_id, friend_id))

        # Shuffle
        random.shuffle(possible_friendships)

        for i in range(
                num_users * avg_friendships // 2):  # > bindirectional (2)
            friendships = possible_friendships[i]
            self.add_friendship(friendships[0], friendships[1])

    def populate_graph2(self, num_users, avg_friendships):
        """ Faster runtime """

        # Reset graph
        self.reset()

        # Add users
        for i in range(num_users):
            self.add_user(f"User {i}")

        # How many friendships we want
        target_friendships = num_users * avg_friendships

        # How many we have
        total_friendships = 0

        collisions = 0

        while total_friendships < target_friendships:
            user_id = random.randint(1, self.last_id)
            friend_id = random.randint(1, self.last_id)

            if self.add_friendship(user_id, friend_id):
                total_friendships += 2
            else:
                collisions += 1

        print("COLLISIONS:", collisions)

    def get_neighbors(self, friend_id):
        """ Find friends to assist in get_all_social_paths"""
        return self.friendships[friend_id]

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME

        # Can implement queue object to reserve first-in-first out order
        # (degrees of sep)
        q = Queue()
        # Start queue with used id
        q.enqueue([user_id])

        # while there's something in the queue
        while q.size() > 0:

            # Pop first item from queue
            current = q.dequeue()

            # Declare vertex/node
            vertex = current[-1]

            # Check if its been visited
            if vertex not in visited:
                visited[vertex] = current

                # if not visited yet, check its neighbors (should be friends)
                # will need a get_neighbors function
                for neighbor in self.get_neighbors(vertex):
                    q.enqueue(current + [neighbor])

        return visited


if __name__ == '__main__':
    # sg = SocialGraph()
    # sg.populate_graph(10, 2)
    # # print("---" * 10)
    # # print(sg.users)
    # print("---" * 10)
    # print(sg.friendships)
    # print("---" * 10)
    # connections = sg.get_all_social_paths(1)
    # print(connections)

    # ```
    sg = SocialGraph()
    sg.populate_graph2(100, 2)
    # print("FRIENDSHIPS")
    print(sg.friendships)
    # print("---" * 10)
    # # {1: {8, 10, 5}, 2: {10, 5, 7}, 3: {4}, 4: {9, 3}, 5: {8, 1, 2}, 6: {10}, 7: {2}, 8: {1, 5}, 9: {4}, 10: {1, 2, 6}}
    # connections = sg.get_all_social_paths(1)
    # print("CONNECTIONS")
    # print(connections)
    # print("---" * 10)
    # {1: [1], 8: [1, 8], 10: [1, 10], 5: [1, 5], 2: [1, 10, 2], 6: [1, 10, 6], 7: [1, 10, 2, 7]}
    # ```
    # Note that in this sample, Users 3, 4 and 9 are not in User 1's extended
    # social network.
