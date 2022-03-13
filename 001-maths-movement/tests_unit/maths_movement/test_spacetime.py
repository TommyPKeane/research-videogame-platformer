import operator
import sys

from maths_movement import spacetime

import pytest


@pytest.mark.parametrize(
    "init, expected",
    (
        (0, 0),
        (1, float("+Inf")),
        (-1, float("-Inf")),
        (10, float("+Inf")),
        (sys.float_info.epsilon, float("+Inf")),
        (-sys.float_info.epsilon, float("-Inf")),
    )
)
def test_Direction_init(init, expected):
    d = spacetime.Direction(init)
    assert d == expected


@pytest.mark.parametrize(
    "init, comparator, comparison, expected",
    (
        (0, operator.gt, 0, False),
        (0, operator.ge, 0, True),
    )
)
def test_Direction_gte(init, comparator, comparison, expected):
    d = spacetime.Direction(init)
    assert comparator(d, comparison) is expected
