from algorithms import binary_search_tree
from domain.binary_tree_node import BinaryTreeNode


def test_insert(with_tracker):
    inputs = [76, 21, 4, 32, 100, 64, 52]
    expected = [50, 76, 21, 4, 32, 100, 64, 52]

    root_node = BinaryTreeNode(value=50)
    for _, v in enumerate(inputs):
        new_node = BinaryTreeNode(value=v)
        binary_search_tree.insert(root_node, new_node)

    assert True
