from abc import abstractmethod
from typing import Self, List

import numpy as np
from loguru import logger


class Node(object):
    """
    :param parent:
        The parent node of this node.

        None if root.

    :param children:
        The child nodes of this node.

    :param puzzle:
        The puzzle with the size of [3][3], which needs to be solved.
        It can contain numbers from 0-8, where 0 is an empty field and the other numbers are values.

    :param seed:
        A value which can be used to generate the same random puzzle over and over again for multiple instances.
    """

    def __init__(self, parent: Self = None, children: List[Self] = None, puzzle: np.ndarray = None, seed: int = None):
        self.parent = parent
        self.children = children

        if self.is_root():
            self.puzzle = self.__create_random_puzzle(seed)
        else:
            if puzzle is None:
                raise ValueError("Puzzle cannot be None")

            self.puzzle = puzzle

    @staticmethod
    def __create_random_puzzle(seed: int = None) -> np.ndarray:
        rng = np.random.default_rng(seed)

        numbers = np.arange(9)
        rng.shuffle(numbers)

        puzzle = np.reshape(numbers, (3, 3))
        return puzzle

    def is_root(self) -> bool:
        if self.parent is None:
            return True
        else:
            return False

    def is_puzzle_solvable(self) -> bool:
        raise NotImplementedError()

    @abstractmethod
    def create_search_tree(self) -> None:
        pass

    def find_solution_in_search_tree(self) -> np.ndarray:
        raise NotImplementedError()


