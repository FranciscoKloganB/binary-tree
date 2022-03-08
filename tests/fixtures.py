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
