from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from typing import Any, Callable


@dataclass
class BinaryTreeNode:
    parent: BinaryTreeNode | None
    left: BinaryTreeNode | None
    right: BinaryTreeNode | None
    value: Any

    @property
    def has_left(self):
        return self.left is not None

    @property
    def has_right(self):
        return self.right is not None

    @property
    def has_parent(self):
        return self.parent is not None

    @property
    def is_leaf(self):
        return not (self.has_left or self.has_right)


class BinaryTreeCallableProgram:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __call__(node: BinaryTreeNode):
        raise NotImplementedError(
            "Classes inheriting from BinaryTreeCallableProgram must implement __call__(node: BinaryTreeNode) method"
        )


def traverse_depth_first_search_pre_order(node: BinaryTreeNode, fn: Callable):
    """Performs a DFS traversal in pre-order approach over a binary tree

    Traversal computes visited values as they are seen by prioritizing paths
    to the left. When left is not available, backtracks and attempts to follow
    right paths.

    Left paths are prioritized whenever available.
    """
    fn(node.value)

    if node.has_left:
        traverse_depth_first_search_pre_order(node.left)

    if node.has_right:
        traverse_depth_first_search_pre_order(node.right)


def traverse_depth_first_search_in_order(node: BinaryTreeNode, fn: Callable):
    """Performs a DFS traversal in in-order approach over a binary tree

    Values of the tree are computed bottom to top giving priority to left nodes,
    then immidiate parents of leaf left nodes and then, right nodes. I.e., node
    values are computed whenever all their left children have been computed.
    """
    if node.has_left():
        traverse_depth_first_search_in_order(node.left)

    fn(node.value)

    if node.has_left():
        traverse_depth_first_search_in_order(node.right)


def traverse_depth_first_search_post(node: BinaryTreeNode, fn: Callable):
    """Performs a DFS traversal in post-order approach over a binary tree

    Values are computed bottom to top, giving priority to left nodes, then
    right nodes and then, parents. I.e., node values are computed whenever
    all their children have already been computed.
    """
    if node.has_left():
        traverse_depth_first_search_in_order(node.left)

    if node.has_left():
        traverse_depth_first_search_in_order(node.right)

    fn(node.value)


def traverse_breath_first_search(node: BinaryTreeNode, fn: Callable):
    """Performs a BFS traversal over a binary tree

    Values of the tree are computed as they are visited. All tree nodes on a given
    depth level are computed before any children below that depth level is computed.
    """
    queue = deque()
    queue.append(node)

    while queue.count > 0:
        current_node = queue.popleft()

        fn(current_node.value)

        if current_node.has_left:
            queue.append(current_node.left)

        if current_node.has_right:
            queue.append(current_node.right)
