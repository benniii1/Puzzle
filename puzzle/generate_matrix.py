import numpy as np


class GenerateMatrix:
    @staticmethod
    def generate_goal_state():
        # Generates the goal state matrix for the 8-puzzle problem
        goal_matrix = np.arange(9).reshape((3, 3))
        return goal_matrix

    @staticmethod
    def generate_random_state(seed: int = None) -> np.ndarray:
        # Generates a random initial state matrix for the 8-puzzle problem.
        rng = np.random.default_rng(seed)

        numbers = np.arange(9)
        rng.shuffle(numbers)

        puzzle = np.reshape(numbers, (3, 3))
        return puzzle
