from enum import Enum
from typing import Any

from domain.binary_tree_node import BinaryTreeNode


class DeleteResponse(Enum):
    DELETED = 1
    NONE = 0
    SUCCESS = -1


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
    the target was found and is the only node in the tree.
    """
    target = find(value)

    if target is None:
        return DeleteResponse.NONE

    if target.parent is None and target.is_leaf():
        return DeleteResponse.LAST_NODE

    if target.parent is None:
        raise NotImplementedError(
            "this is the root of the tree - verify if there are subtrees act accordingly"
        )

    if target.is_leaf():
        return delete_leaf(target)

    if target.parent.has_single_child():
        return delete_and_patch_single_child(target)

    return delete_and_patch_siblings(target)


def delete_leaf(target: BinaryTreeNode) -> int:
    if target.parent.left == target:
        target.parent.left = None
    else:
        target.parent.right = None

    return DeleteResponse.SUCCESS


def delete_and_patch_single_child(target: BinaryTreeNode) -> int:
    if target.has_left:
        target.parent.left = target.left
    else:
        target.parent.right = target.right

    return DeleteResponse.SUCCESS


def delete_and_patch_siblings(target: BinaryTreeNode) -> int:
    raise NotImplementedError(
        "must rebalance siblings after deletion with or without AVL constraint"
    )
