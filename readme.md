# Pathfinding Algorithms Repository

This repository contains Python implementations of various pathfinding algorithms, including A*, BFS (Breadth-First Search), and DFS (Depth-First Search). These implementations demonstrate different approaches to solving grid-based and puzzle-based pathfinding problems.

## Files Included

### 1. `a-star.py`
- Implements the A* algorithm to solve puzzles such as the 8-puzzle problem.
- Features Manhattan distance heuristic for estimating the cost to the goal state.
- Includes functions to reconstruct the optimal path and visualize the steps.

### 2. `a-star-comparing_heuristics.py`
- Extends the A* algorithm with support for multiple heuristics:
  - Manhattan distance
  - Misplaced tiles
- Compares the performance and efficiency of these heuristics in solving the 8-puzzle problem.

### 3. `bfs_dfs.py`
- Provides basic implementations of Breadth-First Search (BFS) and Depth-First Search (DFS).
- Designed for use in graph traversal tasks, with examples of finding paths between nodes.

### 4. `bfs-dfs-comparison.py`
- Compares BFS and DFS algorithms in terms of:
  - Time taken to find a path
  - Number of cells or nodes explored
- Includes utility functions to handle grid-based environments with obstacles.

### 5. `bfs-pathfinder.py`
- Implements a BFS algorithm to find the shortest path in a grid-based environment.
- Handles obstacles represented as `X` in the grid.
- Demonstrates efficiency in finding the optimal path from a start to a goal point.

### 6. `dfs-pathfinder.py`
- Implements a DFS algorithm to explore paths in a grid-based environment.
- Provides a non-optimal but effective method for pathfinding with backtracking.

## Usage

Each script can be executed independently. Below are the general steps for running these scripts:

1. Clone this repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project folder:
   ```bash
   cd pathfinding-algorithms
   ```
3. Run the desired script:
   ```bash
   python3 <filename>.py
   ```

## Requirements

- Python 3.x
- Standard libraries such as `heapq`, `collections`, and `time`.

## Features

- Modular implementations for reusability and customization.
- Clear separation of algorithm logic and utility functions.
- Performance comparison between BFS, DFS, and A* algorithms.