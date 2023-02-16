import numpy as np

def say_hello_with_message(msg: str) -> str:
    """Awesome function to say hello with message.

    Args:
        msg (str): The message of your dreams.

    Returns:
        str: The standard sentence with your message.
    """
    print(f"hello, the message is: {msg}")


def wow(msg):
    say_hello_with_message(f"wow: {msg}")

if __name__ == '__main__':
    say_hello_with_message(1)