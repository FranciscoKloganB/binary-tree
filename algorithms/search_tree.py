from typing import Any

from domain.binary_tree_node import BinaryTreeNode


def insert(root_node: BinaryTreeNode, new_node: BinaryTreeNode):
    current_node = root_node

    if new_node.value <= current_node.value and current_node.has_left:
        insert(current_node.left, new_node)
    elif new_node.value <= current_node.value:
        current_node.left = new_node
    elif current_node.has_right:
        insert(current_node.right, new_node)
    else:
        current_node.right = new_node


def find(root_node: BinaryTreeNode, value: Any):

    if value < root_node.value and root_node.has_left:
        find(root_node.left, value)
    if value > root_node.value and root_node.has_right:
        find(root_node.right, value)

    return value == root_node.value
