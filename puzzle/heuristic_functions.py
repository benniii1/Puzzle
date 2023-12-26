import numpy as np
from puzzle.generate_matrix import GenerateMatrix
from puzzle.solvability import is_solvable


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


class HeuristicFunctions:
    @staticmethod
    def manhattan_distance(state) -> int:
        if is_state_solvable:
            distance = 0
            h = ""
            for i in range(3):
                for j in range(3):
                    value = state[i, j]
                    goal_position = np.argwhere(goal_state == value)[0]
                    h += str(abs(i - goal_position[0]) + abs(j - goal_position[1])) + " + "
                    distance += abs(i - goal_position[0]) + abs(j - goal_position[1])
            print("h = ", h[:-2])
            return distance

    @staticmethod
    def hamming_displacement(state, goal) -> int:
        """
        Calculate the number of misplaced tiles heuristic between two states.
        """
        if is_state_solvable:
            misplaced_tiles_count = 0
            for row in range(3):
                for column in range(3):
                    if state[row][column] != goal[row][column]:
                        misplaced_tiles_count += 1
            return misplaced_tiles_count


if __name__ == '__main__':
    if is_state_solvable:
        heuristic_functions = HeuristicFunctions()

        manhattan_dist = heuristic_functions.manhattan_distance(random_state)
        print("Heuristic 1 (Manhattan Distance):", manhattan_dist)

        hamming_displacement = heuristic_functions.hamming_displacement(random_state, goal_state)
        print("\nHeuristic 2 (Hamming Distance):", hamming_displacement)
