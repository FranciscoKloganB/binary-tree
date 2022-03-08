from asyncio.log import logger

from algorithms.bfs import traverse_breath_first_search


def test_traverse_breath_first_search(with_one_to_seven_tree, with_tracker):
    expected = [1, 2, 5, 3, 4, 6, 7]

    traverse_breath_first_search(with_one_to_seven_tree, with_tracker)

    assert with_tracker.order == expected
