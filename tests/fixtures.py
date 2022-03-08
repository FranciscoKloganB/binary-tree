import pytest

from domain.binary_tree_node import BinaryTreeCallableProgram, BinaryTreeNode


@pytest.fixture()
def with_tracker():
    class ComputatedOrder(BinaryTreeCallableProgram):
        def __init__(self):
            self.order = []

        def __call__(self, node: BinaryTreeNode):
            self.order.append(node.value)

    return ComputatedOrder()


@pytest.fixture()
def with_one_to_seven_tree():
    one = BinaryTreeNode(value=1, parent=None)
    two = BinaryTreeNode(value=2, parent=one)
    five = BinaryTreeNode(value=5, parent=one)
    one.left = two
    one.right = five

    three = BinaryTreeNode(value=3, parent=two)
    four = BinaryTreeNode(value=4, parent=two)
    two.left = three
    two.right = four

    six = BinaryTreeNode(value=6, parent=five)
    seven = BinaryTreeNode(value=7, parent=five)
    five.left = six
    five.right = seven

    return one
