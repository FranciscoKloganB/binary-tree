from algorithms import binary_search_tree
from algorithms.binary_tree.dfs import traverse_depth_first_search_pre_order
from domain.binary_tree_node import BinaryTreeNode


def test_insert(with_tracker):
    inputs = [76, 21, 4, 32, 100, 64, 52]
    expected = [50, 21, 4, 32, 76, 64, 52, 100]

    root_value = 50
    root_node = BinaryTreeNode(value=root_value)

    for v in inputs:
        new_node = BinaryTreeNode(value=v)
        binary_search_tree.insert(root_node, new_node)

    traverse_depth_first_search_pre_order(root_node, with_tracker)

    assert with_tracker.order == expected
