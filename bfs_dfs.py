from collections import deque

def bfs(graph, start, goal):
    """
    Perform a breadth-first search to find a path from the start state to the goal state in the given graph.

    The given graph is a dictionary of adjacency lists, where each key is a node and its value is a list of
    neighboring nodes. The start and goal are given as nodes in the graph.

    This function performs a breadth-first search to find a path from the start to the goal. If no path exists, it returns None.

    Parameters:
        graph (dict): The graph in which to search.
        start (node): The starting node.
        goal (node): The goal node.

    Returns:
        list of nodes: A list of nodes representing a path from the start to the goal, or None if no path exists.
    """
    
    visited = []
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            if node == goal:
                return visited
            
            queue.extend(graph[node])
    
    return visited


def dfs(graph, start, goal):
    """
    Perform a depth-first search to find a path from the start state to the goal state in the given graph.

    The given graph is a dictionary of adjacency lists, where each key is a node and its value is a list of
    neighboring nodes. The start and goal are given as nodes in the graph.

    This function performs a depth-first search to find a path from the start to the goal. If no path exists, it returns None.

    Parameters:
        graph (dict): The graph in which to search.
        start (node): The starting node.
        goal (node): The goal node.

    Returns:
        list of nodes: A list of nodes representing a path from the start to the goal, or None if no path exists.
    """
    visited = []
    stack = [start]
    
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            if node == goal:
                return visited
            
            stack.extend(graph[node][::-1])
    
    return visited


graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': ['G'],
    'D': ['H', 'I'],
    'E': ['J'],
    'F': [],
    'G': ['K'],
    'H': [],
    'I': ['L', 'M'],
    'J': [],
    'K': ['N'],
    'L': [],
    'M': ['O', 'P'],
    'N': [],
    'O': [],
    'P': []
}

goal = 'K'

print("BFS:", bfs(graph, 'A', goal))
print("DFS:", dfs(graph, 'A', goal))
            

