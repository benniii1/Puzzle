import heapq


class PuzzleNode:
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


def generate_neighbors(node):
    i, j = get_blank_position(node.state)
    neighbors = []

    for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
        if 0 <= x < 3 and 0 <= y < 3:
            new_state = [row.copy() for row in node.state]
            new_state[i][j], new_state[x][y] = new_state[x][y], new_state[i][j]
            neighbors.append(PuzzleNode(new_state, parent=node, action=(i, j, x, y), cost=node.cost + 1,
                                        heuristic=calculate_heuristic(new_state)))

    return neighbors


def calculate_heuristic(state):
    total_distance = 0
    goal_positions = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), None: (2, 2)  # None represents the empty space
    }

    for i in range(3):
        for j in range(3):
            tile = state[i][j]
            goal_position = goal_positions[tile]
            total_distance += abs(i - goal_position[0]) + abs(j - goal_position[1])

    return total_distance


def is_solvable(state):
    flatten_state = [tile for row in state for tile in row if tile is not None]
    inversions = sum(1 for i in range(len(flatten_state) - 1) for j in range(i + 1, len(flatten_state)) if
                     flatten_state[i] > flatten_state[j])
    return inversions % 2 == 0


def solve_8_puzzle(initial_state, goal_state):
    if not is_solvable(initial_state):
        print("Solvable: No")
        return None

    print("Solvable: Yes")

    initial_node = PuzzleNode(initial_state, heuristic=calculate_heuristic(initial_state))
    priority_queue = [initial_node]

    while priority_queue:
        current_node = heapq.heappop(priority_queue)

        if current_node.state == goal_state:
            # Goal reached, reconstruct the path
            path = []
            while current_node:
                path.append(current_node.action)
                current_node = current_node.parent
            return path[::-1]

        neighbors = generate_neighbors(current_node)
        for neighbor in neighbors:
            heapq.heappush(priority_queue, neighbor)

    return None  # No solution found


# Example usage:
initial_state = [
    [7, 2, 4],
    [5, None, 6],
    [8, 3, 1]
]

goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, None]
]

solution_path = solve_8_puzzle(initial_state, goal_state)
print(solution_path)
