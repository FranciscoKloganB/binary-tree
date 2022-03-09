from turtle import right

from domain.binary_tree_node import BinaryTreeNode


def height(current_node: BinaryTreeNode) -> int:
    """Recursively calculates the height of a tree.

    The height of a tree is given by the length (number of edges) on the longest
    path between the root node of the tree and the deepest leaf node.
    """
    if current_node is None:
        # Stop condition (when we reach a child of a leaf node, that child is None)
        # Minus one
        return -1

    left_height = height(current_node.left)
    right_height = height(current_node.right)

    if left_height > right_height:
        return 1 + left_height

    return 1 + right_height
