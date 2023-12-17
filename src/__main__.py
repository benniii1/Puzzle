from sys import stderr

import numpy as np

from hamming_node import HammingNode
from manhattan_node import ManhattanNode
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

    n = Node()

    logger.debug(f"Type: {type(n)}")
    logger.debug(f"Is Root: {n.is_root()}")
    logger.debug("Puzzle:")
    pretty_log_puzzle(n.puzzle)
    logger.debug("-" * 20)
    logger.debug("-" * 20)

    hn = HammingNode()

    logger.debug(f"Type: {type(hn)}")
    logger.debug(f"Is Root: {hn.is_root()}")
    logger.debug(f"Hamming Distance: {hn.get_hamming_distance()}")
    logger.debug("Puzzle:")
    pretty_log_puzzle(hn.puzzle)
    logger.debug("-" * 20)
    logger.debug("-" * 20)

    """
    This snippet will throw an exception, because the manhattan_distance calculation is not implemented yet.
    
    mn = ManhattanNode()

    logger.debug(f"Type: {type(mn)}")
    logger.debug(f"Is Root: {mn.is_root()}")
    logger.debug("Puzzle:")
    pretty_log_puzzle(mn.puzzle)
    logger.debug("Manhattan Distance:")
    pretty_log_puzzle(mn.get_manhattan_distance())
    logger.debug("-" * 20)
    logger.debug("-" * 20)
    """


def pretty_log_puzzle(puzzle: np.ndarray) -> None:
    for line in puzzle:
        logger.debug(line)


main()
