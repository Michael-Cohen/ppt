import numpy as np


def say_hello_with_message(msg2: str) -> str:
    """Awesome function to say hello with message.

    Args:
        msg2 (str): The message of your dreams.

    Returns:
        str: The standard sentence with your message.
    """
    return f"hello, the message is: {msg2}"


def wow(quantity: float) -> str:
    """Diplays a Numpy array with one element."""
    return f"Numpy result: {np.array([quantity])}"
