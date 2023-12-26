import numpy as np


class GenerateMatrix:
    @staticmethod
    def generate_random_state():
        return np.random.permutation(9).reshape(3, 3)

    @staticmethod
    def generate_goal_state():
        goal_matrix = np.arange(9).reshape((3, 3))
        return goal_matrix
