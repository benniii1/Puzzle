import numpy as np


class GenerateMatrix:
    @staticmethod
    def generate_goal_state():
        goal_matrix = np.arange(9).reshape((3, 3))
        return goal_matrix

    @staticmethod
    def generate_random_state(seed: int = None) -> np.ndarray:
        rng = np.random.default_rng(seed)

        numbers = np.arange(9)
        rng.shuffle(numbers)

        puzzle = np.reshape(numbers, (3, 3))
        return puzzle
