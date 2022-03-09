from domain.binary_tree_node import BinaryTreeNode as Node

HEIGHT_EXAMPLES_TABLE = [
    (
        Node(
            30,
            left=Node(18, left=Node(10), right=Node(25)),
            right=Node(45, right=Node(50)),
        ),
        2,
    ),
    (
        Node(
            30,
            left=Node(18, left=Node(10), right=Node(25)),
            right=Node(45),
        ),
        2,
    ),
    (
        Node(
            30,
            left=Node(
                18,
                left=Node(10, left=Node(5)),
                right=Node(25),
            ),
            right=Node(45),
        ),
        3,
    ),
    (Node(30), 0),
]
