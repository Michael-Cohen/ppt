import sys

import pytest

from pptm.salut import run, say_hello_with_message, wow


def test_say_hello_with_message() -> None:
    assert say_hello_with_message("salut!").startswith("Hello, the message is: salut!")


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


def test_run(monkeypatch, capsys) -> None:
    # Define input message:
    input_msg = "bonjour comment vas-tu?"

    # Set up monkeypatch for sys.argv:
    monkeypatch.setattr(sys, "argv", ["salut.py", input_msg])

    # Call main function:
    run()

    # Capture output:
    captured = capsys.readouterr()

    # Check output:
    assert captured.out.startswith(f"Hello, the message is: {input_msg}")
