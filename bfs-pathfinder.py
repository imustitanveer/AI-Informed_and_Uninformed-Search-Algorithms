from collections import deque

def bfs_shortest_path(grid, start, goal):
    """
    Find the shortest path from start to goal in the given grid.

    The given grid is a 2D list of strings, where 'X' represents an obstacle,
    and any other character represents an open space. The start and goal are
    given as (x, y) coordinates.

    This function performs a breadth-first search to find the shortest path from
    the start to the goal. If no path exists, it returns None.

    Parameters:
        grid (list of lists): The grid in which to search.
        start (tuple): The starting position, given as (x, y) coordinates.
        goal (tuple): The goal position, given as (x, y) coordinates.

    Returns:
        list of tuples: A list of (x, y) coordinates representing the shortest
        path from the start to the goal, or None if no path exists.
    """
    rows, cols = len(grid), len(grid[0])
    queue = deque([(start, [start])])
    visited = set()
    visited.add(start)

    while queue:
        position, path = queue.popleft()

        if position == goal:
            return path

        for neighbor in get_neighbors(position, grid, rows, cols):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    return None 

def get_neighbors(position, grid, rows, cols):
    """
    Find all the neighbors of a given position in the grid.

    Parameters:
        position (tuple): The current position in the grid, given as (x, y) coordinates.
        grid (list of lists): The grid in which we are searching.
        rows (int): The number of rows in the grid.
        cols (int): The number of columns in the grid.

    Returns:
        list of tuples: A list of tuples, each representing a neighbor of the given position. Neighbors are
        given as (x, y) coordinates.

    """
    
    x, y = position
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
    neighbors = []

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] != 'X':  # Check bounds and obstacles
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

path = bfs_shortest_path(grid, start, goal)
print("Shortest Path:", path)