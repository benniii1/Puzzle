from typing import List

import numpy as np

from node import Node


class ManhattanNode(Node):
    __manhattan_distance: np.ndarray

    def __init__(self):
        super().__init__()
        self.__manhattan_distance = np.zeros((3, 3), dtype=int)
        self.__update_manhattan_distance()

    def get_manhattan_distance(self) -> np.ndarray:
        return self.__manhattan_distance

    def __update_manhattan_distance(self) -> None:
        raise NotImplementedError()

    def create_search_tree(self) -> None:
        raise NotImplementedError()
