# Read the maze from a file
def read_maze(filename):
    with open(filename, 'r') as file:
        return [list(line.strip()) for line in file.readlines()]

# Find the entry point 'I'
def find_entry(maze):
    for col in range(len(maze[0])):
        if maze[0][col] == 'I':
            return (0, col)
    return None

# Recursive function to find the exit
def find_exit(maze, position):
    row, col = position
    
    # Base cases
    if maze[row][col] == 'O':  # Exit found
        return True
    if maze[row][col] in ('#', 'X'):  # Wall or visited path
        return False
    
    # Mark as visited
    maze[row][col] = 'X'
    
    # Explore possible moves (down, up, right, left)
    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < len(maze) and 0 <= new_col < len(maze[0]):
            if find_exit(maze, (new_row, new_col)):
                return True
    
    # Unmark if no path was found (backtracking)
    maze[row][col] = ' '
    return False

# Solve the maze
def solve_maze(filename):
    maze = read_maze(filename)
    entry = find_entry(maze)
    
    if entry is None:
        print("No entry point found in the maze.")
        return
    
    if find_exit(maze, entry):
        print("The exit was found! Here is one possible path:")
    else:
        print("No path to the exit was found.")
    
    for row in maze:
        print(''.join(row))

# Example usage
if __name__ == "__main__":
    solve_maze("maze.txt")