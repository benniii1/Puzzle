from sys import stderr
from typing import Any, List

import numpy as np
from loguru import logger
import time

from puzzle.a_star_search import a_star_search
from puzzle.generate_matrix import GenerateMatrix
from puzzle.solvability import is_solvable
from puzzle.heuristic_functions import HeuristicFunctions
from memory_profiler import memory_usage


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
    logger.add(sink=stderr, level="INFO")  # Configures the log handler.

    # Uncomment the following line to see the moves, but comment out line 36 before running this file.
    # logger.add(sink=stderr, level="DEBUG")

    logger.info("Let's start!")

    goal_state: np.ndarray = GenerateMatrix.generate_goal_state()

    logger.debug("Goal State:")
    pretty_log_puzzle(goal_state)

    count_solvable_puzzles: int = 0
    manhattan_time_total: List[float] = []
    hamming_time_total: List[float] = []
    manhattan_memory_total: List[Any] = []
    hamming_memory_total: List[Any] = []
    for _ in range(100):
        logger.info("-" * 40)
        logger.info(f"Run #{_}")
        logger.info("-" * 40)
        logger.info("-" * 40)

        random_state: np.ndarray = GenerateMatrix.generate_random_state()

        logger.debug("Random State:")
        pretty_log_puzzle(random_state)

        is_state_solvable: bool = is_solvable(random_state)
        logger.debug(f"Is Solvable: {is_state_solvable}")

        if is_solvable(random_state):
            count_solvable_puzzles += 1
            logger.info("A* Search with Manhattan Distance Heuristic")
            logger.info("-" * 40)

            manhattan_start_time = time.time()

            # Calculate memory usage and get result
            manhattan_memory, manhattan_dist_path = memory_usage(
                (a_star_search, (random_state, goal_state, HeuristicFunctions.manhattan_distance)), retval=True)

            manhattan_end_time = time.time()

            manhattan_time = manhattan_end_time - manhattan_start_time
            manhattan_time_total.append(manhattan_time)

            logger.info(f"Run Time: {manhattan_time}s")

            manhattan_memory_total.append(max(manhattan_memory))
           
            logger.info(f"Memory Used: {max(manhattan_memory)}MB")

            for state, move in manhattan_dist_path:
                logger.debug(f"Move: {move}")
                pretty_log_puzzle(state)

            logger.info("-" * 40)
            logger.info("A* Search with Hamming Distance Heuristic")
            logger.info("-" * 40)

            hamming_start_time = time.time()

            # Calculate memory usage
            hamming_memory, hamming_displacement_path = memory_usage(
                (a_star_search, (random_state, goal_state, HeuristicFunctions.hamming_displacement)), retval=True)

            hamming_end_time = time.time()

            hamming_time = hamming_end_time - hamming_start_time
            hamming_time_total.append(hamming_time)

            logger.info(f"Run Time: {hamming_time}s")

            hamming_memory_total.append(max(hamming_memory))

            logger.info(f"Memory Used: {max(hamming_memory)}MB")

            for state, move in hamming_displacement_path:
                logger.debug(f"Move: {move}")
                pretty_log_puzzle(state)
        else:
            logger.warning("The random state is not solvable.")

    logger.info("-" * 40)
    logger.info("-" * 40)
    logger.info("-" * 15 + " Summary " + "-" * 16)
    logger.info("-" * 40)
    logger.info("-" * 40)
    logger.info(f"Solvable Puzzles: {count_solvable_puzzles}")
    logger.info(f"Execution Time (Total): {np.sum(manhattan_time_total + hamming_time_total)}s")
    logger.info("-" * 40)

    if count_solvable_puzzles > 0:
        logger.info("Manhattan Distance")
        logger.info(f"Execution Time (Total): {np.sum(manhattan_time_total)}s")
        logger.info(f"Execution Time (Mean): {np.mean(manhattan_time_total)}s")
        logger.info(f"Execution Time (Standard Deviation): {np.std(manhattan_time_total)}s")
        logger.info(f"Memory Usage (Mean): {np.mean(manhattan_memory_total)}MB")
        logger.info(f"Memory Usage (Standard Deviation): {np.std(manhattan_memory_total)}MB")

        logger.info("-" * 40)

        logger.info("Hamming Distance")
        logger.info(f"Execution Time (Total): {np.sum(hamming_time_total)}s")
        logger.info(f"Execution Time (Mean): {np.mean(hamming_time_total)}s")
        logger.info(f"Execution Time (Standard Deviation): {np.std(hamming_time_total)}s")
        logger.info(f"Memory Usage (Mean): {np.mean(hamming_memory_total)}MB")
        logger.info(f"Memory Usage (Standard Deviation): {np.std(hamming_memory_total)}MB")


def pretty_log_puzzle(puzzle: np.ndarray) -> None:
    for line in puzzle:
        logger.debug(line)


if __name__ == "__main__":
    main()
