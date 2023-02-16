import numpy as np


def say_hello_with_message(msg: str) -> None:
    """Awesome function to say hello with message.

    Args:
        msg (str): The message of your dreams.

    Returns:
        str: The standard sentence with your message.
    """
    print(f"hello, the message is: {msg}")


def wow(quantity: float) -> str:
    """Diplays a Numpy array with one element."""
    return f"Numpy result: {np.array([quantity])}"


if __name__ == "__main__":
    say_hello_with_message("1")
