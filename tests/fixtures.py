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
    one = BinaryTreeNode(parent=None, left=None, right=None, value=1)
    two = BinaryTreeNode(parent=one, left=None, right=None, value=2)
    five = BinaryTreeNode(parent=one, left=None, right=None, value=5)
    one.left = two
    one.right = five

    three = BinaryTreeNode(parent=two, left=None, right=None, value=3)
    four = BinaryTreeNode(parent=two, left=None, right=None, value=4)
    two.left = three
    two.right = four

    six = BinaryTreeNode(parent=five, left=None, right=None, value=6)
    seven = BinaryTreeNode(parent=five, left=None, right=None, value=7)
    five.left = six
    five.right = seven

    return one
