from typing import Any

from domain.binary_tree_node import BinaryTreeNode


def insert(current_node: BinaryTreeNode, new_node: BinaryTreeNode):
    if new_node.value <= current_node.value and current_node.has_left:
        insert(current_node.left, new_node)
    elif new_node.value <= current_node.value:
        current_node.left = new_node
    elif current_node.has_right:
        insert(current_node.right, new_node)
    else:
        current_node.right = new_node


def find(current_node: BinaryTreeNode, value: Any) -> BinaryTreeNode | None:
    if value < current_node.value and current_node.has_left:
        return find(current_node.left, value)

    if value > current_node.value and current_node.has_right:
        return find(current_node.right, value)

    return current_node if value == current_node.value else None


def delete(current_node: BinaryTreeNode, value: Any) -> int:
    """Finds the node to be deleted and removes it from the binary tree.

    The method returns value `0` if the the target `value` does not exist in the Tree.
    Value `1` if the `value` was found and deleted successfully. It returns `-1` if
    the target was find and is the only node in the tree.
    if the value is last element of the Tree.
    """
    target = find(value)

    if target is None:
        return 0

    if target.is_leaf:
        return handle_leaf_deletion(target, target.parent)

    if target.parent.has_single_child():
        return handle_single_child_deletion(target, target.parent)


def handle_leaf_deletion(target: BinaryTreeNode, parent: BinaryTreeNode | None) -> int:
    if parent is None:
        return -1

    if parent.left == target:
        parent.left = None
    else:
        parent.right = None

    return 1


def handle_single_child_deletion(target: BinaryTreeNode, parent: BinaryTreeNode) -> int:

