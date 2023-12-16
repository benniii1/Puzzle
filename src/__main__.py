from sys import stderr
from node import Node
from loguru import logger


def main():
    """
    The entry point of the program.

    :return:
    """

    """
    Loguru Log Levels:
    
    | Level name | Severity value | Logger method    |
    |------------|----------------|------------------|
    | TRACE      | 5              | logger.trace()   |
    | DEBUG      | 10             | logger.debug()   |
    | INFO       | 20             | logger.info()    |
    | SUCCESS    | 25             | logger.success() |
    | WARNING    | 30             | logger.warning() |
    | ERROR      | 40             | logger.error()   |
    | CRITICAL   | 50             | logger.critical()|
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
    logger.debug(f"Is root? {n.is_root_node()}")


main()
