def dfs_find_path(grid, start, goal):
    """
    Perform a depth-first search to find a path from the start state to the goal state in the given grid.

    The given grid is a 2D list of strings, where 'X' represents an obstacle,
    and any other character represents an open space. The start and goal are
    given as (x, y) coordinates.

    This function performs a depth-first search to find a path from the start to the goal. If no path exists, it returns None.

    Parameters:
        grid (list of lists): The grid in which to search.
        start (tuple): The starting position, given as (x, y) coordinates.
        goal (tuple): The goal position, given as (x, y) coordinates.

    Returns:
        list of tuples: A list of (x, y) coordinates representing a path from the start to the goal, or None if no path exists.
    """

    stack = [(start, [start])]
    visited = set()

    while stack:
        position, path = stack.pop()

        if position == goal:
            return path

        if position not in visited:
            visited.add(position)
            for neighbor in get_neighbors(position, grid):
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))

    return None

def get_neighbors(position, grid):
    """
    Find all valid neighboring positions from the current position in the grid.

    Parameters:
        position (tuple): The current position in the grid, represented as (x, y) coordinates.
        grid (list of lists): The grid where 'X' represents an obstacle, and other characters represent open spaces.

    Returns:
        list of tuples: A list of (x, y) coordinates representing valid neighboring positions.
    """
    x, y = position
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    neighbors = []

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] != 'X':
            neighbors.append((nx, ny))

    return neighbors

grid = [
    ['S', '0', '0', 'X', '0'],
    ['0', 'X', '0', 'X', '0'],
    ['0', '0', '0', 'X', 'G'],
    ['X', 'X', '0', '0', '0'],
    ['0', '0', 'X', 'X', '0']
]

start = (0, 0)
goal = (2, 4)

path = dfs_find_path(grid, start, goal)
print("Path found by DFS:", path)
