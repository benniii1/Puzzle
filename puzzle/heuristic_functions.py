import numpy as np
from puzzle.generate_matrix import GenerateMatrix
from puzzle.solvability import is_solvable


class HeuristicFunctions:
    @staticmethod
    def manhattan_distance(state, goal) -> int:
        """
        Calculates the Manhattan Distance heuristic between the original state and the goal state
        """
        distance = 0
        h = ""
        for i in range(3):
            for j in range(3):
                value = state[i, j]
                goal_position = np.argwhere(goal == value)[0]
                h += str(abs(i - goal_position[0]) + abs(j - goal_position[1])) + " + "
                distance += abs(i - goal_position[0]) + abs(j - goal_position[1])
        # print("h = ", h[:-2])
        return distance

    @staticmethod
    def hamming_displacement(state, goal) -> int:
        """
        Calculates the number of misplaced tiles heuristic (Hamming Distance) between two states
        """
        misplaced_tiles_count = 0
        for row in range(3):
            for column in range(3):
                if state[row][column] != goal[row][column]:
                    misplaced_tiles_count += 1
        return misplaced_tiles_count
