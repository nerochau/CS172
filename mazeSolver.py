#PAIR PROJECT 3: MAZE SOLVER
#SAMPHASNEARYROTH CHAU (NERO) & MAYA GUPTA-LEMUS

FILENAME = 'maze.txt'

def main():
    maze = read_maze(FILENAME)
    print("Original Maze:")
    print_maze(maze)
    
    start_pos = find_start(maze)
    if start_pos:
        if find_exit(maze, start_pos):
            print("\nThere is an exit! Here is the path:")
        else:
            print("\nNo exit found.")
        print_maze(maze)  # Print maze with path
    else:
        print("No entrance found in the maze.")

def read_maze(filename):
    """Reads the maze from a file and returns it as a list of lists."""
    with open(filename) as f:
        return [list(line.strip()) for line in f]

def print_maze(maze):
    """Prints the maze."""
    for row in maze:
        print("".join(row))

def find_start(maze):
    """Finds the entry position (I) in the top row of the maze."""
    for j in range(len(maze[0])):
        if maze[0][j] == 'I':
            return (0, j)  # Return row and column of entrance
    return None

def find_exit(maze, pos):
    """recursive function to find the exit and mark path"""
    x, y = pos
    
    # Base cases
    if not (0 <= x < len(maze) and 0 <= y < len(maze[0])):  # outside of bound
        return False
    if maze[x][y] == 'O':  # Found exit
        return True
    if maze[x][y] in ('#', 'X'):  # hit wall or already visited
        return False
    
    maze[x][y] = 'X' #symbol to show part of the path
    
    # Try moving in all four directions
    if (find_exit(maze, (x + 1, y)) or  # Down
        find_exit(maze, (x, y + 1)) or  # Right
        find_exit(maze, (x, y - 1)) or  # Left
        find_exit(maze, (x - 1, y))):   # Up
        return True
    
    # Unmark if no exit found (backtrack)
    maze[x][y] = ' '
    return False

if __name__ == "__main__":
    main()