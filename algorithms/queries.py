from typing import List, Tuple

from domain.binary_tree_node import BinaryTreeNode


def height(current_node: BinaryTreeNode) -> int:
    """Recursively calculates the height of a tree.

    The height of a tree is given by the length (number of edges) on the longest
    path between the root node of the tree and the deepest leaf node.
    """
    if current_node is None:
        # Stop condition (when we reach a child of a leaf node, that child is None)
        return -1

    left_height = height(current_node.left)
    right_height = height(current_node.right)

    if left_height > right_height:
        return 1 + left_height

    return 1 + right_height


def is_balanced_tree(
    root_node: BinaryTreeNode,
) -> Tuple[bool, BinaryTreeNode | None]:
    """Asserts if all subtrees of the current tree are balanced.

    A tree is balanced if the difference in height between LST and RST is (-1, 0, 1).

    Returns (True, None) if the tree is balanced, otherwise (False, BinaryTreeNode) is
    returned where BinaryTreeNode is the root of a subtree which violates the balance
    constraint. Note: the method returns at most one broken subtree root_node, but there
    may be more.
    """
    if root_node is None:
        # If this is the child of a leaf (there is nothing to check)
        return True, None

    height_diff = height(root_node.left) - height(root_node.right)

    if abs(height_diff) > 1:
        # If any subtree pair breaks the constraint, the tree is not balanced
        return False, root_node

    lst_is_balanced, lst_root = is_balanced_tree(root_node.left)
    rst_is_balanced, rst_root = is_balanced_tree(root_node.right)

    if lst_is_balanced and rst_is_balanced:
        return True, None

    if not lst_is_balanced:
        return False, lst_root

    if not rst_is_balanced:
        return False, rst_root
