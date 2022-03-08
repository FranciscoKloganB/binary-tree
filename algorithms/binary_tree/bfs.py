from collections import deque
from typing import Callable

from domain.binary_tree_node import BinaryTreeNode


def traverse_breath_first_search(node: BinaryTreeNode, fn: Callable):
    """Performs a BFS traversal over a binary tree

    Values of the tree are computed as they are visited. All tree nodes on a given
    depth level are computed before any children below that depth level is computed.
    """
    queue = deque()
    queue.append(node)

    while len(queue) > 0:
        current_node = queue.popleft()

        fn(current_node)

        if current_node.has_left:
            queue.append(current_node.left)

        if current_node.has_right:
            queue.append(current_node.right)
