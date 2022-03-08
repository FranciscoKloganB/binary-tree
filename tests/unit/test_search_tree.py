import pytest

from algorithms.dfs import traverse_depth_first_search_pre_order
from algorithms.search_tree import find, insert
from domain.binary_tree_node import BinaryTreeNode

@pytest.fixture()
def with_binary_search_tree():
    root_value = 50
    root_node = BinaryTreeNode(value=root_value)

    remaining_values = [76, 21, 4, 32, 100, 64, 52]

    for v in remaining_values:
        new_node = BinaryTreeNode(value=v)
        insert(root_node, new_node)

    return root_node

def test_insert_placement_order_is_correct(with_binary_search_tree, with_tracker):
    expected = [50, 21, 4, 32, 76, 64, 52, 100]

    traverse_depth_first_search_pre_order(with_binary_search_tree, with_tracker)

    assert with_tracker.order == expected


@pytest.mark.parametrize(
    "target, expected",
    [
        (-1, False),
        (0, False),
        (1, False),
        (2, False),
        (3, False),
        (4, True),
        (21, True),
        (52, True),
        (100, True),
        (1000, False),
    ],
)
def test_find_is_correct(with_binary_search_tree, target, expected):
    assert find(with_binary_search_tree, target) == expected
