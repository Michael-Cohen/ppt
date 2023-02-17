import pytest

from pptm.salut import say_hello_with_message, wow


def test_say_hello_with_message() -> None:
    assert say_hello_with_message("salut!") == "hello, the message is: salut!"


@pytest.mark.parametrize(
    "quantity, result",
    [
        (4.0, "[4.]"),
        (0.0, "[0.]"),
        (-1.0, "[-1.]")  # this last pair is purposefully wrong so we can
        # show an example of the pytest error message
    ],
)
def test_is_even(quantity: float, result: str) -> None:
    assert wow(quantity) == f"Numpy result: {result}"
