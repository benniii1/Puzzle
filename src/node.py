class Node:
    def __init__(self, parent=None, children=None, puzzle=None):
        self.parent = parent
        self.children = children
        self.puzzle = puzzle

    def __str__(self):
        return str(self.__dict__)