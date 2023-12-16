from sys import stderr
from node import Node
from loguru import logger


def main():
    """
    The entry point of the program.

    :return:
    """
    logger.remove()  # Removes the default handler, so that we can set a log level without duplicating messages.
    logger.add(sink=stderr, level="DEBUG")  # Configures the log handler.
    logger.info("Let's start!")

    n = Node(parent=None,
             puzzle=[
                 [0, 1, 2],
                 [3, 4, 5],
                 [6, 7, 8]
             ])

    n.pretty_print_puzzle()


main()
