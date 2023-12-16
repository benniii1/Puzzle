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

        Example:
             [0, 1, 2],
             [3, 4, 5],
             [6, 7, 8]
    """
    def __init__(self, parent=None, children=None, puzzle=None):
        self.parent = parent
        self.children = children
        self.puzzle = puzzle

    def __str__(self):
        return str(self.__dict__)

    def pretty_print_puzzle(self):
        for line in self.puzzle:
            logger.debug(line)

    def is_root_node(self):
        if self.parent is None:
            return True
        else:
            return False
