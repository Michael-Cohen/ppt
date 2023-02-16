import numpy as np

def say_hello_with_message(msg: str) -> str:
    """Awesome function to say hello with message.

    Args:
        msg (str): The message of your dreams.

    Returns:
        str: The standard sentence with your message.
    """
    print(f"hello, the message is: {msg}")


def wow(quantity):
    print(f"Numpy result: {np.array([quantity])}")

if __name__ == '__main__':
    say_hello_with_message(1)