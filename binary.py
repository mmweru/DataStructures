import collections


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data is None:
            self.data = data
        else:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)


# Inorder traversal
def inOrderPrint(r):
    if r is None:
        return
    else:
        inOrderPrint(r.left)
        print(r.data, end=' ')
        inOrderPrint(r.right)


# Preorder traversal
def preOrderPrint(r):
    if r is None:
        return
    else:
        print(r.data, end=' ')
        preOrderPrint(r.left)
        preOrderPrint(r.right)


# PostOrderPrint
def postOrderPrint(r):
    if r is None:
        return
    else:
        postOrderPrint(r.left)
        postOrderPrint(r.right)
        print(r.data, end=' ')


# Adjacency List
def makeList(r):
    if r is None:
        return
    else:
        d[r.data] = []
        makeList(r.left)
        if r.left:
            d[r.data].append(r.left.data)
        if r.right:
            d[r.data].append(r.right.data)
        makeList(r.right)
    return d


#Breadth first

def bfs(al):
    queue = collections.deque('g')
    visited = []

    while queue:
        node = queue.popleft()
        visited.append(node)
        [queue.append(x) for x in al[node]]
    print(visited)

if __name__ == '__main__':
    root = Node('g')
    root.insert('c')
    root.insert('b')
    root.insert('a')
    root.insert('e')
    root.insert('d')
    root.insert('f')
    root.insert('i')
    root.insert('h')
    root.insert('k')

    d = {}
    aList = makeList(root)
    print(aList)