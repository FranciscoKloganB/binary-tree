from cmath import exp
import pytest

from algorithms.queries import height, is_balanced_tree
from tests.unit.examples.balance_examples import BALANCE_EXAMPLES_TABLE
from tests.unit.examples.height_examples import HEIGHT_EXAMPLES_TABLE


@pytest.mark.parametrize("root_node, expected", HEIGHT_EXAMPLES_TABLE)
def test_height_calculates_size_correctly(root_node, expected):
    assert height(root_node) == expected


@pytest.mark.parametrize("root_node, expected_bool, expected_type", BALANCE_EXAMPLES_TABLE)
def test_is_balanced_tree(root_node, expected_bool, expected_type):
    result_bool, result_node = is_balanced_tree(root_node)

    assert result_bool == expected_bool
    assert isinstance(result_node, expected_type)
