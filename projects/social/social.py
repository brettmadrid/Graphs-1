import random
import time


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if (self.size()) > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


class User:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


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
            return False
        # if either are already in the friendship dictionary, the friendship already exists
        # since the SocialGraph is an undirected graph
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
            return False
        else:
            # else add bi-directional relationship to the graph
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)
            return True

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        # automatically increment the ID to assign the new user
        self.last_id += 1
        # add new user to dictionary key: id, value: name
        self.users[self.last_id] = User(name)
        # add new user to friendships dictionary - key: id, value: empty set
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

        # 100 users, avg 10 friendships each
        # avg_friendships = total_friendships / num_users
        
        # Add users
        for i in range(num_users):
            self.add_user(f"User {i+1}")

        # create N random friendships, with all possible friendship combinations
        possible_friendships = []
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append((user_id, friend_id))

        # shuffle the list
        random.shuffle(possible_friendships)

        print(possible_friendships)

        # then grab the first N elements from the list.
        # number of times to call add_friendships = avg_friendships * num_users / 2
        for i in range(num_users * avg_friendships // 2):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        # Note that this is a dictionary, not a set
        visited = {}
        # using a BST
        q = Queue()
        # load user_id in an array to store path
        q.enqueue([user_id])
        while q.size() > 0:
            path = q.dequeue()
            # get last user/friend added to the path
            newuser_id = path[-1]
            # if friend has not already been searched
            if newuser_id not in visited:
                # add newuser_id to visited dictionary
                # key: user/friend id, value: path to that user/friend
                visited[newuser_id] = path
                # for each friend of newly added friend...
                for friend in self.friendships[newuser_id]:
                    # if that friend's friends have not already been visited
                    if friend not in visited:
                        # make a copy of the existing path of friends
                        new_path = list(path)
                        # add each new friend's friends to the path
                        new_path.append(friend)
                        # update the search queue with the new path of friends
                        q.enqueue(new_path)
        # will return dictionary of all friends that have been visited
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    start_time = time.time()
    sg.populate_graph(1000, 5)
    end_time = time.time()
    print(f'runtime: {end_time - start_time} seconds')
    connections = sg.get_all_social_paths(1)
    print(connections)
