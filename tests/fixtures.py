import pytest

from domain.binary_tree_node import BinaryTreeCallableProgram, BinaryTreeNode

@pytest.fixture()
def with_computed_order_tracker():
    class ComputatedOrder(BinaryTreeCallableProgram):
        def __init__(self):
            self.order = []

        def __call__(self, node: BinaryTreeNode):
            self.order.append(node.value)

    return ComputatedOrder()


@pytest.fixture()
def with_one_through_seven_tree():
    one = BinaryTreeNode(1)
    two = BinaryTreeNode(2)
    three = BinaryTreeNode(3)
    four = BinaryTreeNode(4)
    five = BinaryTreeNode(5)
    six = BinaryTreeNode(6)
    seven = BinaryTreeNode(7)

    one.left = two
    one.right = five
    two.left = three
    two.right = four
    five.left = six
    five.right = seven
    
    return one
