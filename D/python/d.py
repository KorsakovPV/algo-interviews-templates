from typing import List


class Node():
    def __init__(self):
        self.value = None
        self.up = None
        self.down = None
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.value)

    def __str__(self):
        return self.value


def height(node):
    if node is None:
        return 0
    else:
        return max(height(node.left), height(node.right), height(node.up), height(node.down)) + 1


def get_longest_increasing_path(matrix, n, m) -> int:
    tree = []

    for i in range(n):
        for j in range(m):
            node = Node()
            node.value = matrix[i][j]
            tree.append(node)

    for i in range(n):
        for j in range(m):
            # left
            if 0 <= j - 1 < m and matrix[i][j] < matrix[i][j - 1]:
                tree[i * m + j].left = tree[i * m + j - 1]
            # right
            if 0 <= j + 1 < m and matrix[i][j] < matrix[i][j + 1]:
                tree[i * m + j].right = tree[i * m + j + 1]
            # up
            if 0 <= i - 1 < n and matrix[i][j] < matrix[i - 1][j]:
                tree[i * m + j].up = tree[(i - 1) * m + j]
            # down
            if 0 <= i + 1 < n and matrix[i][j] < matrix[i + 1][j]:
                tree[i * m + j].down = tree[(i + 1) * m + j]

    return max([height(node) for node in tree])


def read_matrix():
    n, m = map(int, input().split())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().split())))
    return matrix, n, m


matrix, n, m = read_matrix()
# matrix, n, m = [[10, 8, 5], [10, 5, 4]], 2, 3
# matrix, n, m = [[1, 1], [1, 1]], 2, 2
# matrix, n, m = [[10, 9], [9, 11]], 2, 2
print(get_longest_increasing_path(matrix, n, m))
