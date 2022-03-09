from unittest import mock

from domain.binary_tree_node import BinaryTreeNode as Node

NoneType = type(None)
NodeType = Node

BALANCE_EXAMPLES_TABLE = [
    (Node(50), True, NoneType),
    (Node(50, left=Node(25)), True, NoneType),
    (Node(50, left=Node(25), right=Node(75)), True, NoneType),
    (Node(50, left=Node(25, left=Node(12)), right=Node(75)), True, NoneType),
    (
        Node(50, left=Node(25, left=Node(12, left=Node(6)), right=Node(14))),
        False,
        NodeType,
    ),
    (
        Node(
            50,
            left=Node(25, left=Node(12, left=Node(6)), right=Node(14)),
            right=Node(75),
        ),
        False,
        NodeType,
    ),
]
