from algorithms.dfs import (
    traverse_depth_first_search_in_order,
    traverse_depth_first_search_post_order,
    traverse_depth_first_search_pre_order,
)


def test_traverse_depth_first_search_pre_order(with_one_to_seven_tree, with_tracker):
    expected = [1, 2, 3, 4, 5, 6, 7]

    traverse_depth_first_search_pre_order(with_one_to_seven_tree, with_tracker)

    assert with_tracker.order == expected


def test_traverse_depth_first_search_in_order(with_one_to_seven_tree, with_tracker):
    expected = [3, 2, 4, 1, 6, 5, 7]

    traverse_depth_first_search_in_order(with_one_to_seven_tree, with_tracker)

    assert with_tracker.order == expected


def test_traverse_depth_first_search_post_order(with_one_to_seven_tree, with_tracker):
    expected = [3, 4, 2, 6, 7, 5, 1]

    traverse_depth_first_search_post_order(with_one_to_seven_tree, with_tracker)

    assert with_tracker.order == expected
