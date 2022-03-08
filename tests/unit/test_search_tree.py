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
    "target",
    [
        (-1),
        (0),
        (1),
        (2),
        (3),
        (1000),
    ],
)
def test_find_returns_none_when_target_does_not_exist(with_binary_search_tree, target):
    assert find(with_binary_search_tree, target) is None


@pytest.mark.parametrize(
    "target",
    [
        (4),
        (21),
        (52),
        (100),
    ],
)
def test_find_returns_target_when_it_exists(with_binary_search_tree, target):
    assert find(with_binary_search_tree, target) is not None
