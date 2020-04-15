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

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        # Use add_user num_users times

        # Create friendships
        for i in range(0, num_users):
            self.add_user(f"User {i+1}")

        # Generate all friendship combinations
        possible_friendships =  []

        # Avoid dupes by making sure first number is smaller than second
        for user_id in self.users:
            for friend_id in range(user_id+1, self.last_id+1):
                possible_friendships.append((user_id, friend_id))

        # Shuffle all possible friendships
        random.shuffle(possible_friendships)

        # Create for first X pairs x is total //2
        for i in range(num_users * avg_friendships // 2):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])

        # * Hint 1: To create N random friendships, you could create a
        # list with all possible friendship combinations, shuffle the
        # list, then grab the first N elements from the list. You will
        # need to `import random` to get shuffle.
        # * Hint 2: `add_friendship(1, 2)` is the same as
        # `add_friendship(2, 1)`. You should avoid calling one after
        # the other since it will do nothing but print a warning. You
        # can avoid this by only creating friendships where user1 < user2.

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set

        def bfs(start_user, dest_user):
            # create queue and enqueue start_user
            queue = Queue()
            queue.enqueue([start_user])
            # create visited set
            inner_visited = set()
            # while queue not empty
            while queue.size() > 0:
                # dequeue path
                path = queue.dequeue()
                if not path[-1] in inner_visited:
                    # add to visited
                    inner_visited.add(path[-1])
                # if last user in path = dest_user
                if path[-1] == dest_user:
                    # return path
                    return path
                # enqueue friends
                for friend in self.friendships[path[-1]]:
                    # if friend not in visited
                    if not friend in inner_visited:
                        # create copy of path
                        new_path = list(path)
                        # add neighbor to it
                        new_path.append(friend)
                        # enqueue it
                        queue.enqueue(new_path)

        # do a bfs on each user
        for user in self.users:
            path = bfs(user_id, user)
            visited[user] = path
            
        # clean out non friends (None type)
        for friend in self.users:
            if not visited[friend]:
                del visited[friend]

        # no friends?
        if len(visited) <= 1:
            print(f'\nUser {user_id} has no friends. :,(\n')
            return visited
        else:
            return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print([user for user in sg.users])
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
