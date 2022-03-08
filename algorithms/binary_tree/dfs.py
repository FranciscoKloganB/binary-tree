from typing import Callable

from domain.binary_tree_node import BinaryTreeNode


def traverse_depth_first_search_pre_order(node: BinaryTreeNode, fn: Callable):
    """Performs a DFS traversal in pre-order approach over a binary tree

    Traversal computes visited values as they are seen by prioritizing paths
    to the left. When left is not available, backtracks and attempts to follow
    right paths.

    Left paths are prioritized whenever available.
    """
    fn(node)

    if node.has_left:
        traverse_depth_first_search_pre_order(node.left, fn)

    if node.has_right:
        traverse_depth_first_search_pre_order(node.right, fn)


def traverse_depth_first_search_in_order(node: BinaryTreeNode, fn: Callable):
    """Performs a DFS traversal in in-order approach over a binary tree

    Values of the tree are computed bottom to top giving priority to left nodes,
    then immidiate parents of leaf left nodes and then, right nodes. I.e., node
    values are computed whenever all their left children have been computed.
    """
    if node.has_left:
        traverse_depth_first_search_in_order(node.left, fn)

    fn(node)

    if node.has_left:
        traverse_depth_first_search_in_order(node.right, fn)


def traverse_depth_first_search_post_order(node: BinaryTreeNode, fn: Callable):
    """Performs a DFS traversal in post-order approach over a binary tree

    Values are computed bottom to top, giving priority to left nodes, then
    right nodes and then, parents. I.e., node values are computed whenever
    all their children have already been computed.
    """
    if node.has_left:
        traverse_depth_first_search_in_order(node.left, fn)

    if node.has_left:
        traverse_depth_first_search_in_order(node.right, fn)

    fn(node)
