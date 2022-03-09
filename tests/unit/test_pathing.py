from turtle import right

import pytest

from algorithms.pathing import height
from domain.binary_tree_node import BinaryTreeNode


@pytest.mark.parametrize(
    "root_node, expected",
    [
        (
            BinaryTreeNode(
                30,
                left=BinaryTreeNode(
                    18, left=BinaryTreeNode(10), right=BinaryTreeNode(25)
                ),
                right=BinaryTreeNode(45, right=BinaryTreeNode(50)),
            ),
            2,
        ),
        (
            BinaryTreeNode(
                30,
                left=BinaryTreeNode(
                    18, left=BinaryTreeNode(10), right=BinaryTreeNode(25)
                ),
                right=BinaryTreeNode(45),
            ),
            2,
        ),
        (
            BinaryTreeNode(
                30,
                left=BinaryTreeNode(
                    18,
                    left=BinaryTreeNode(10, left=BinaryTreeNode(5)),
                    right=BinaryTreeNode(25),
                ),
                right=BinaryTreeNode(45),
            ),
            3,
        ),
        (BinaryTreeNode(30), 0),
    ],
)
def test_height_calculates_size_correctly(root_node, expected):
    assert height(root_node) == expected
