import numpy as np

from node import Node


class HammingNode(Node):
    __hamming_distance: int

    def __init__(self):
        super().__init__()
        self.update_hamming_distance()

    def get_hamming_distance(self) -> int:
        return self.__hamming_distance

    def update_hamming_distance(self) -> None:
        sorted_puzzle = np.reshape(np.arange(9), (3, 3))
        self.__hamming_distance = np.count_nonzero(self.puzzle != sorted_puzzle)

    def create_search_tree(self) -> None:
        raise NotImplementedError()
