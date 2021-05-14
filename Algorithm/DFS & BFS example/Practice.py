from collections import deque


# Node Class
class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

    def __str__(self):
        return '({} {} {})'.format(self.data, self.left, self.right)


# Binary Search Tree Class
class BST(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert_value(self.root, data)
        return self.root is not None

    def _insert_value(self, node, data):
        if node is None:
            node = Node(data)

        else:
            if data <= node.data:
                node.left = self._insert_value(node.left, data)
            else:
                node.right = self._insert_value(node.right, data)

        return node


# DFS
def dfs(node):
    global N, answer

    if N == 1:
        answer = node.data
        return

    if node.left:
        N -= 1
        dfs(node.left)
    if node.right:
        N -= 1
        dfs(node.right)


# BFS
def bfs(node):
    global N, answer, queue

    if N == 1:
        answer = node.data
        return

    if node.left:
        queue.append(node.left)
    if node.right:
        queue.append(node.right)

    while len(queue) > 0:
        N -= 1
        next_node = queue.popleft()
        bfs(next_node)


N = 0
answer = 0
queue = deque()

if __name__ == "__main__":
    f_input = open("input3.txt", 'r')
    f_output = open("output.txt", 'w')
    T = int(f_input.readline())

    for _ in range(T):
        temp = f_input.readline().strip()
        if not temp: break

        # N is the number for target index and the type of algorithm
        algorithm = temp[-6:-3]
        N = int(temp[-2])
        answer = 0

        data_list = list(map(int, f_input.readline().split()))
        if not data_list: break

        # Make a BST by using data
        tree = BST()
        for data in data_list:
            tree.insert(data)

        # Use the DFS or BFS algorithm
        if algorithm == "dfs":
            dfs(tree.root)

        if algorithm == "bfs":
            bfs(tree.root)

        # Write the answers on output.txt
        f_output.write(str(answer) + "\n")

    f_input.close()
    f_output.close()
