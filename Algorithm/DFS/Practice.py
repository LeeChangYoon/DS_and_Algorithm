dfs_pre, dfs_post, dfs_in = [], [], []


# Node
class Node(object):
    def __init__(self, idx, data):
        self.idx = idx
        self.data = data
        self.left = self.right = None

    def __str__(self):
        return '({} {} {})'.format(self.data, self.left, self.right)


# BST
class BST(object):
    def __init__(self):
        self.root = None

    def insert(self, idx, data):
        self.root = self._insert_value(self.root, idx, data)
        return self.root is not None

    def _insert_value(self, node, idx, data):
        if node is None:
            node = Node(idx, data)

        else:
            if data <= node.data:
                node.left = self._insert_value(node.left, idx, data)
            else:
                node.right = self._insert_value(node.right, idx, data)

        return node


# Pre-order
def pre_order(node):
    global dfs_pre

    dfs_pre.append(node.idx)
    if node.left:
        pre_order(node.left)
    if node.right:
        pre_order(node.right)


# In-order
def in_order(node):
    global dfs_in

    if node.left:
        in_order(node.left)
    dfs_in.append(node.idx)
    if node.right:
        in_order(node.right)


# Post-order
def post_order(node):
    global dfs_post

    if node.left:
        post_order(node.left)
    if node.right:
        post_order(node.right)
    dfs_post.append(node.idx)


# Solution
def solution(nodeinfo):
    for i in range(len(nodeinfo)):
        nodeinfo[i] = [i + 1] + nodeinfo[i]

    nodeinfo = sorted(nodeinfo, key=lambda x: x[-1], reverse=True)

    tree = BST()
    for idx, data, _ in nodeinfo:
        tree.insert(idx, data)

    # Pre-order
    pre_order(tree.root)

    # Post-order
    post_order(tree.root)

    return [pre, post]


print(solution([[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]]))
