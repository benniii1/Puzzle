import heapq


class NodePuzzle:
    def __init__(self, state, parent=None, action=None, cost=0, heuristic=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost
        self.heuristic = heuristic

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)


def get_blank_position(state):
    for i, row in enumerate(state):
        for j, tile in enumerate(row):
            if tile is None:
                return i, j


def count_inversions(state):
    inversions = 0
    flatten_state = [tile for row in state for tile in row if tile is not None]

    for i in range(len(flatten_state) - 1):
        for j in range(i + 1, len(flatten_state)):
            if flatten_state[i] > flatten_state[j]:
                inversions += 1

    return inversions


def is_solvable(state):
    inversions = count_inversions(state)
    return inversions % 2 == 0


def generate_neighbors(node):
    i, j = get_blank_position(node.state)
    neighbors = []

    for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
        if 0 <= x < 3 and 0 <= y < 3:
            new_state = [row.copy() for row in node.state]
            new_state[i][j], new_state[x][y] = new_state[x][y], new_state[i][j]
            neighbors.append(NodePuzzle(new_state, parent=node, action=((i, j), (x, y)), cost=node.cost + 1,
                                        heuristic=calculate_heuristic_hamming(new_state)))

    return neighbors


def calculate_heuristic_hamming(state):
    goal_state = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, None]
    ]

    hamming_distance = 0

    for i in range(3):
        for j in range(3):
            if state[i][j] != goal_state[i][j] and state[i][j] is not None:
                hamming_distance += 1

    return hamming_distance


def format_move(move):
    if move is not None:
        (row1, col1), (row2, col2) = move
        return f"({row1}, {col1}) to ({row2}, {col2})"
    else:
        return "No solution found"


def solve_8_puzzle_hamming(initial_state, goal_state):
    if not is_solvable(initial_state):
        print("Solvable: No")
        return None

    print("Solvable: Yes")

    initial_node = NodePuzzle(initial_state, heuristic=calculate_heuristic_hamming(initial_state))
    priority_queue = [initial_node]

    while priority_queue:
        current_node = heapq.heappop(priority_queue)

        if current_node.state == goal_state:
            # Goal reached, reconstruct the path
            path = []
            while current_node:
                path.append(current_node.action)
                current_node = current_node.parent
            return [format_move(move) for move in path[::-1]]

        neighbors = generate_neighbors(current_node)
        for neighbor in neighbors:
            heapq.heappush(priority_queue, neighbor)

    return None  # No solution found


# Example usage:
initial_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, None]
]

goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [None, 7, 8]
]

solution_path_hamming = solve_8_puzzle_hamming(initial_state, goal_state)
print(solution_path_hamming)
