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
    logger.add(sink=stderr, level="DEBUG")  # Configures the log handler.

    logger.info("Let's start!")

    goal_state: np.ndarray = GenerateMatrix.generate_goal_state()

    manhattan_memory_usage = []
    hamming_memory_usage = []

    manhattan_execution_time = []
    hamming_execution_time = []

    for _ in range(3):
        random_state: np.ndarray = GenerateMatrix.generate_random_state()

        logger.debug("Random State:")
        pretty_log_puzzle(random_state)

        logger.debug("Goal State:")
        pretty_log_puzzle(goal_state)

        is_state_solvable: bool = is_solvable(random_state)
        print("\nIs the random state solvable?", is_state_solvable)
        print()

        if is_solvable(random_state):
            # A* Search with Manhattan Distance Heuristic
            print("A* Search with Manhattan Distance Heuristic:")
            manhattan_start_time = time.time()
            manhattan_dist_path = a_star_search(random_state, goal_state, HeuristicFunctions.manhattan_distance)
            manhattan_end_time = time.time()
            manhattan_total_time = manhattan_end_time - manhattan_start_time
            manhattan_execution_time.append(manhattan_total_time)

            print("Run Time:", manhattan_total_time, "seconds\n")

            manhattan_memory_used = memory_usage(
                (a_star_search, (random_state, goal_state, HeuristicFunctions.manhattan_distance)))

            manhattan_memory_usage.append(max(manhattan_memory_used))

            print("Memory Used:", max(manhattan_memory_used), "MB")

            for state, move in manhattan_dist_path:
                print("Move:", move)
                print(state)
                print()

            # A* Search with Hamming Distance Heuristic
            print("\nA* Search with Hamming Distance Heuristic:")
            hamming_start_time = time.time()
            hamming_displacement_path = a_star_search(random_state, goal_state, HeuristicFunctions.hamming_displacement)
            hamming_end_time = time.time()
            hamming_total_time = hamming_end_time - hamming_start_time

            print("Run Time:", hamming_total_time, "seconds\n")

            # Calculate memory usage
            hamming_memory_used = memory_usage(
                (a_star_search, (random_state, goal_state, HeuristicFunctions.hamming_displacement)))

            hamming_memory_usage.append(max(hamming_memory_used))

            print("Memory Used:", max(hamming_memory_used), "MB")

            for state, move in hamming_displacement_path:
                print("Move:", move)
                print(state)
                print()
        else:
            print("The random state is not solvable.\n")

    print("\nMean Memory Usage (Manhattan Distance Heuristic):", np.mean(manhattan_memory_usage), "MB")
    print("Standard Deviation of Memory Usage (Manhattan Distance Heuristic):", np.std(manhattan_memory_usage), "MB")
    print("Mean Execution Time (Manhattan Distance Heuristic):", np.mean(manhattan_execution_time), "seconds")
    print("Standard Deviation of Execution Time (Manhattan Distance Heuristic):", np.std(manhattan_execution_time),
          "seconds\n")

    print("\nMean Memory Usage (Hamming Distance Heuristic):", np.mean(hamming_memory_usage), "MB")
    print("Standard Deviation of Memory Usage (Hamming Distance Heuristic):", np.std(hamming_memory_usage), "MB")
    print("Mean Execution Time (Hamming Distance Heuristic):", np.mean(hamming_execution_time), "seconds")
    print("Standard Deviation of Execution Time (Hamming Distance Heuristic):", np.std(hamming_execution_time),
          "seconds\n")


def pretty_log_puzzle(puzzle: np.ndarray) -> None:
    for line in puzzle:
        logger.debug(line)


main()
