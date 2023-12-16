import numpy as np
from loguru import logger


class Node:
    """
    parent:
        The parent node.

        None if root.

    children:
        The child nodes.

    puzzle:
        The puzzle with the size of [3][3], which needs to be solved.
        It can contain numbers from 0-8, where 0 is an empty field and the other numbers are values.
    """

    _is_root_assigned = False
    hamming_distance = 0

    def __init__(self, parent=None, children=None):
        if parent is None and Node._is_root_assigned:
            raise ValueError("Only one node can be root!")

        self.parent = parent
        self.children = children
        self.puzzle = self.__create_random_puzzle()
        self.update_hamming_distance()

        if self.is_root():
            Node._is_root_assigned = True

    @staticmethod
    def __create_random_puzzle():
        rng = np.random.default_rng()

        numbers = np.arange(9)
        rng.shuffle(numbers)

        puzzle = np.reshape(numbers, (3, 3))
        return puzzle

    def pretty_print_puzzle(self):
        for line in self.puzzle:
            print(line)

    def is_root(self):
        if self.parent is None:
            return True
        else:
            return False

    def update_hamming_distance(self):
        sorted_puzzle = np.reshape(np.arange(9), (3, 3))
        self.hamming_distance = np.count_nonzero(self.puzzle != sorted_puzzle)
