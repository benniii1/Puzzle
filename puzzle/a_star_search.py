import numpy as np
import heapq
from puzzle.generate_matrix import GenerateMatrix
from puzzle.solvability import is_solvable
from puzzle.heuristic_functions import HeuristicFunctions


class Puzzle:
    def __init__(self, state, parent=None, move=None, depth=0, cost=0):
        self.state = state
        self.parent = parent
        self.move = move
        self.depth = depth
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost

    def __eq__(self, other):
        return np.array_equal(self.state, other.state)

    def generate_successors(self):
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
        return self.depth + heuristic_function(self.state, goal_state)


def a_star_search(initial_state, goal_state, heuristic_function):
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
            # print('path', path)
            return path[::-1]

        successors = current_puzzle.generate_successors()

        for successor in successors:
            if tuple(map(tuple, successor.state)) not in closed_set:
                successor.cost = successor.calculate_cost(heuristic_function, goal_state)
                heapq.heappush(open_set, successor)

    return None


if __name__ == '__main__':
    # Generate the random and goal states
    random_state = GenerateMatrix.generate_random_state()
    goal_state = GenerateMatrix.generate_goal_state()

    print("Random State:")
    print(random_state)
    print()
    print("Goal State:")
    print(goal_state)

    is_state_solvable = is_solvable(random_state)
    print("\nIs the random state solvable?", is_state_solvable)
    print()

    if is_solvable(random_state):
        manhattan_dist_path = a_star_search(random_state, goal_state, HeuristicFunctions.manhattan_distance)
        print("A* Search with Manhattan Distance Heuristic:")
        for state, move in manhattan_dist_path:
            print("Move:", move)
            print(state)
            print()

        hamming_displacement_path = a_star_search(random_state, goal_state, HeuristicFunctions.hamming_displacement)
        print("\nA* Search with Hamming Distance Heuristic:")
        for state, move in hamming_displacement_path:
            print("Move:", move)
            print(state)
            print()
    else:
        print("The random state is not solvable.")
