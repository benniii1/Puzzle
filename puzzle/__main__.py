from sys import stderr
import numpy as np
from loguru import logger
import time

from puzzle.a_star_search import a_star_search
from puzzle.generate_matrix import GenerateMatrix
from puzzle.solvability import is_solvable
from puzzle.heuristic_functions import HeuristicFunctions
from memory_profiler import profile, memory_usage


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

    logger.info("Let's start!")

    goal_state: np.ndarray = GenerateMatrix.generate_goal_state()

    logger.debug("Goal State:")
    pretty_log_puzzle(goal_state)

    #    manhattan_memory_usage = []
    #    hamming_memory_usage = []

    count_solvable_puzzles: int = 0
    manhattan_time_total: int = 0
    hamming_time_total: int = 0
    for _ in range(100):
        logger.info(f"Run #{_}")
        logger.info("-" * 40)

        random_state: np.ndarray = GenerateMatrix.generate_random_state()

        logger.debug("Random State:")
        pretty_log_puzzle(random_state)

        is_state_solvable: bool = is_solvable(random_state)
        logger.debug(f"Is Solvable: {is_state_solvable}")

        if is_solvable(random_state):
            count_solvable_puzzles += 1
            logger.info("A* Search with Manhattan Distance Heuristic")

            manhattan_start_time = time.time()
            manhattan_dist_path = a_star_search(random_state, goal_state, HeuristicFunctions.manhattan_distance)
            manhattan_end_time = time.time()
            manhattan_time = manhattan_end_time - manhattan_start_time
            manhattan_time_total += manhattan_time

            logger.info(f"Run Time: {manhattan_time}s")

            """
            # Calculate memory usage
            manhattan_memory_used = memory_usage(
                (a_star_search, (random_state, goal_state, HeuristicFunctions.manhattan_distance)))

            manhattan_memory_usage.append(max(manhattan_memory_used))
           
            logger.debug(f"Memory Used: {max(manhattan_memory_used)}MB")
            """

            for state, move in manhattan_dist_path:
                logger.debug(f"Move: {move}")
                pretty_log_puzzle(state)

            logger.info("A* Search with Hamming Distance Heuristic")
            hamming_start_time = time.time()
            hamming_displacement_path = a_star_search(random_state, goal_state, HeuristicFunctions.hamming_displacement)
            hamming_end_time = time.time()
            hamming_time = hamming_end_time - hamming_start_time
            hamming_time_total += hamming_time

            logger.info(f"Run Time: {hamming_time}s")

            """
            # Calculate memory usage
            hamming_memory_used = memory_usage(
                (a_star_search, (random_state, goal_state, HeuristicFunctions.hamming_displacement)))

            hamming_memory_usage.append(max(hamming_memory_used))

            logger.debug(f"Memory Used: {max(hamming_memory_used)}MB")
            """

            for state, move in hamming_displacement_path:
                logger.debug(f"Move: {move}")
                pretty_log_puzzle(state)
        else:
            logger.warning("The random state is not solvable.")

    logger.info("-" * 40)
    logger.info("-" * 40)
    logger.info(f"Solvable Puzzles: {count_solvable_puzzles}")
    logger.info(f"Manhattan Time Total: {manhattan_time_total}s")
    logger.info(f"Hamming Time Total: {hamming_time_total}s")


"""
    logger.debug(f"Mean Memory Usage (Manhattan Distance Heuristic): {np.mean(manhattan_memory_usage)}MB")
    logger.debug(f"Standard Deviation of Memory Usage (Manhattan Distance Heuristic): {np.std(manhattan_memory_usage)}"
                 f"MB")
    logger.debug(f"Mean Execution Time (Manhattan Distance Heuristic): {np.mean(manhattan_execution_time)}s")
    logger.debug(f"Standard Deviation of Execution Time (Manhattan Distance Heuristic): "
                 f"{np.std(manhattan_execution_time)}s")

    logger.debug(f"Mean Memory Usage (Hamming Distance Heuristic): {np.mean(hamming_memory_usage)}MB")
    logger.debug(f"Standard Deviation of Memory Usage (Hamming Distance Heuristic): {np.std(hamming_memory_usage)}MB")
    logger.debug("Mean Execution Time (Hamming Distance Heuristic):", np.mean(hamming_execution_time), "seconds")
    logger.debug(f"Standard Deviation of Execution Time (Hamming Distance Heuristic): "
                 f"{np.std(hamming_execution_time)}s")
"""


def pretty_log_puzzle(puzzle: np.ndarray) -> None:
    for line in puzzle:
        logger.debug(line)


main()
