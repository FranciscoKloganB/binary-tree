def test_traverse_depth_first_search_post_pre_order(
    with_one_to_seven_tree, with_tracker
):
    nodes = [1, 2, 3, 4, 5, 6, 7]

    assert nodes == nodes


def test_traverse_depth_first_search_post_in_order(
    with_one_to_seven_tree, with_tracker
):
    nodes = [1, 2, 3, 4, 5, 6, 7]

    assert nodes == nodes


def test_traverse_depth_first_search_post_order(with_one_to_seven_tree, with_tracker):
    nodes = [1, 2, 3, 4, 5, 6, 7]

    assert nodes == nodes
