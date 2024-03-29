import numpy as np
import heapq
from loguru import logger


class Puzzle:
    def __init__(self, state, parent=None, move=None, depth=0, cost=0):
        """
        Initializes a Puzzle object with the given state, parent, move, depth, and cost
        """
        self.state = state
        self.parent = parent
        self.move = move
        self.depth = depth
        self.cost = cost

    def __lt__(self, other):
        """
        Compares two Puzzle objects based on their cost for heap operations in A* search
        """
        if np.isnan(self.cost) or np.isnan(other.cost):
            return False
        return self.cost < other.cost

    def __eq__(self, other):
        # Checks if two Puzzle objects are equal based on their state
        return np.array_equal(self.state, other.state)

    def generate_successors(self):
        """
        Generates the next stage of Puzzle objects by moving the empty space in valid directions
        """
        successors = []
        empty_space = np.argwhere(self.state == 0)[0]

        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Right, Left, Down, Up

        for move in moves:
            new_position = empty_space + move
            if 0 <= new_position[0] < 3 and 0 <= new_position[1] < 3:
                new_state = np.copy(self.state)
                new_state[empty_space[0], empty_space[1]] = new_state[new_position[0], new_position[1]]
                new_state[new_position[0], new_position[1]] = 0
                successors.append(Puzzle(new_state, self, move, self.depth + 1, 0))
        return successors

    def calculate_cost(self, heuristic_function, goal_state):
        """
        Calculates the cost of the current state based on the given heuristic function and the goal state
        """
        cost = self.depth + heuristic_function(self.state, goal_state)
        return cost if not np.isnan(cost) and np.isfinite(cost) else 0.0


def a_star_search(initial_state, goal_state, heuristic_function):
    """
    Performs A* search to find the path from the initial state to the goal state using the given heuristic function
    """
    initial_puzzle = Puzzle(initial_state)
    goal_puzzle = Puzzle(goal_state)

    open_set = [initial_puzzle]
    closed_set = set()

    while open_set:
        current_puzzle = heapq.heappop(open_set)
        closed_set.add(tuple(map(tuple, current_puzzle.state)))

        if np.array_equal(current_puzzle.state, goal_puzzle.state):
            path = []
            while current_puzzle:
                path.append((current_puzzle.state, current_puzzle.move))
                current_puzzle = current_puzzle.parent
            logger.info(f"Number of Nodes Expanded: {len(closed_set)}")
            return path[::-1]

        successors = current_puzzle.generate_successors()

        for successor in successors:
            if tuple(map(tuple, successor.state)) not in closed_set:
                successor.cost = successor.calculate_cost(heuristic_function, goal_state)
                heapq.heappush(open_set, successor)

    return None
