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


def find(current_node: BinaryTreeNode, value: Any):
    if value < current_node.value and current_node.has_left:
        return find(current_node.left, value)

    if value > current_node.value and current_node.has_right:
        return find(current_node.right, value)

    return current_node if value == current_node.value else None


def delete(current_node: BinaryTreeNode, value: Any, once: bool = True):
    pass
