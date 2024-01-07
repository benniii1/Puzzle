import unittest
import numpy as np
from puzzle.a_star_search import a_star_search
from puzzle.generate_matrix import GenerateMatrix
from puzzle.heuristic_functions import HeuristicFunctions
from puzzle.solvability import is_solvable


class TestAStarSearch(unittest.TestCase):

    def setUp(self):
        """
        Set up common test variables.
        Initializes initial and goal states for testing A* search algorithms.
        """
        self.initial_state = GenerateMatrix.generate_random_state(seed=1)
        self.goal_state = GenerateMatrix.generate_goal_state()

    def test_a_star_search_with_manhattan_distance(self):
        """
        Calls the A* search algorithm with the Manhattan Distance heuristic.
        Asserts that a solution is found and the last state in the solution path is the goal state.

        :return: None
        """

        # Call A* search with Manhattan Distance heuristic
        result = a_star_search(self.initial_state, self.goal_state, HeuristicFunctions.manhattan_distance)

        # Assert that the result is not None, indicating a solution was found
        self.assertIsNotNone(result)

        # Assert that the last state in the solution path is equal to the goal state
        self.assertTrue(np.array_equal(result[-1][0], self.goal_state))

    def test_a_star_search_with_hamming_distance(self):
        """
        Calls the A* search algorithm with the Hamming Distance heuristic.
        Asserts that a solution is found and the last state in the solution path is the goal state.

        :return: None
        """

        # Call A* search with Hamming Distance heuristic
        result = a_star_search(self.initial_state, self.goal_state, HeuristicFunctions.hamming_displacement)

        # Assert that the result is not None, indicating a solution was found
        self.assertIsNotNone(result)

        # Assert that the last state in the solution path is equal to the goal state
        self.assertTrue(np.array_equal(result[-1][0], self.goal_state))

    def test_is_solvable(self):
        """
        Defines solvable and unsolvable puzzle instances.
        Calls the is_solvable function and asserts that solvable and unsolvable puzzles are correctly identified.

        :return: None
        """

        # Define solvable and unsolvable puzzle instances
        solvable_puzzle = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
        unsolvable_puzzle = np.array([[1, 2, 3], [4, 5, 8], [7, 6, 0]])

        # Call is_solvable function
        result_solvable = is_solvable(solvable_puzzle)
        result_unsolvable = is_solvable(unsolvable_puzzle)

        # Assert that solvable puzzle is detected as solvable
        self.assertTrue(result_solvable)

        # Assert that unsolvable puzzle is detected as unsolvable
        self.assertFalse(result_unsolvable)

    def test_generate_matrix(self):
        """
        Calls the generate_random_state function with a specific seed and asserts that the generated matrix is not None.

        :return: None
        """

        # Call generate_random_state with a specific seed
        random_state = GenerateMatrix.generate_random_state(seed=42)

        # Assert that the generated matrix is not None
        self.assertIsNotNone(random_state)


if __name__ == '__main__':
    unittest.main()
