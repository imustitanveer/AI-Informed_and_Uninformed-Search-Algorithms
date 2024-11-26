import time
from collections import deque

def bfs(grid, start, goal):
    """
    Perform a breadth-first search to find a path from the start state to the goal state in the given grid.

    The given grid is a 2D list of strings, where 'X' represents an obstacle,
    and any other character represents an open space. The start and goal are
    given as (x, y) coordinates.

    This function performs a breadth-first search to find a path from the start to the goal. If no path exists, it returns None.

    Parameters:
        grid (list of lists): The grid in which to search.
        start (tuple): The starting position, given as (x, y) coordinates.
        goal (tuple): The goal position, given as (x, y) coordinates.

    Returns:
        tuple: A tuple containing the path from the start to the goal, represented as a list of (x, y) coordinates, and the number of explored nodes.
    """
    rows, cols = len(grid), len(grid[0])
    queue = deque([(start, [start])])
    visited = set()
    visited.add(start)
    explored = 0

    while queue:
        position, path = queue.popleft()
        explored += 1

        if position == goal:
            return path, explored

        for neighbor in get_neighbors(position, grid, rows, cols):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    return None, explored


def dfs(grid, start, goal):
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
        tuple: A tuple containing the path from the start to the goal, represented as a list of (x, y) coordinates, and the number of explored nodes.
    """
    stack = [(start, [start])]
    visited = set()
    explored = 0

    while stack:
        position, path = stack.pop()
        explored += 1

        if position == goal:
            return path, explored

        if position not in visited:
            visited.add(position)
            for neighbor in get_neighbors(position, grid):
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))

    return None, explored


def get_neighbors(position, grid, rows=None, cols=None):
    """
    Find all valid neighboring positions from the current position in the grid.

    The given grid is a 2D list of strings, where 'X' represents an obstacle,
    and any other character represents an open space. The start and goal are
    given as (x, y) coordinates.

    Parameters:
        position (tuple): The current position in the grid, represented as (x, y) coordinates.
        grid (list of lists): The grid in which to search.
        rows (int): The number of rows in the grid.
        cols (int): The number of columns in the grid.

    Returns:
        list of tuples: A list of (x, y) coordinates representing valid neighboring positions.
    """
    x, y = position
    rows = rows or len(grid)
    cols = cols or len(grid[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    neighbors = []

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] != 'X':
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

start_time = time.time()
bfs_path, bfs_explored = bfs(grid, start, goal)
bfs_time = time.time() - start_time

start_time = time.time()
dfs_path, dfs_explored = dfs(grid, start, goal)
dfs_time = time.time() - start_time

print("BFS:")
print("Path:", bfs_path)
print("Cells Explored:", bfs_explored)
print("Time Taken:", bfs_time, "seconds")

print("\nDFS:")
print("Path:", dfs_path)
print("Cells Explored:", dfs_explored)
print("Time Taken:", dfs_time, "seconds")
