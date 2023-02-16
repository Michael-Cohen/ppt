import pytest

from src.ppt.salut import wow


@pytest.mark.parametrize(
    "quantity, result",
    [
        (5.0, "[5.]"),
        (0.0, "[0.]"),
        (-1.0, "[-1.]")  # this last pair is purposefully wrong so we can
        # show an example of the pytest error message
    ],
)
def test_is_even(quantity: float, result: str) -> None:
    assert wow(quantity) == f"Numpy result: {result}"
