from loguru import logger


class Node:
    def __init__(self, parent=None, children=None, puzzle=None):
        self.parent = parent
        self.children = children
        self.puzzle = puzzle

    def __str__(self):
        return str(self.__dict__)

    def pretty_print_puzzle(self):
        for line in self.puzzle:
            logger.info(line)
