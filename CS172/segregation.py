#SAMPHASNEARYROTH CHAU & MAYA GUPTA-LEMUS

import random
from graphics import GraphWin, Rectangle, Point

# Parameters
GRID_SIZE = 20
CELL_SIZE = 20
WINDOW_SIZE = GRID_SIZE * CELL_SIZE

SIMILARITY_THRESHOLD = 0.3
RED_RATIO = 0.5
BLUE_RATIO = 0.5
EMPTY_RATIO = 0.1

# Colors
EMPTY = 0
RED = 1
BLUE = 2
COLOR_MAP = {EMPTY: "white", RED: "red", BLUE: "blue"}

def initialize_grid():
    '''mixing the colors'''
    num_cells = GRID_SIZE * GRID_SIZE
    num_empty = int(num_cells * EMPTY_RATIO)
    num_red = (num_cells - num_empty) // 2
    num_blue = num_cells - num_empty - num_red

    agents = [RED] * num_red + [BLUE] * num_blue + [EMPTY] * num_empty
    random.shuffle(agents)

    grid = [agents[i * GRID_SIZE:(i + 1) * GRID_SIZE] for i in range(GRID_SIZE)]
    return grid

def get_neighbors(grid, x, y):
    neighbors = []
    grid_size = len(grid)
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            nx, ny = x + dx, y + dy
            if 0 <= nx < grid_size and 0 <= ny < grid_size:
                neighbors.append(grid[nx][ny])
    return neighbors

def is_satisfied(grid, x, y):
    '''to find if nerighbor is satisfied'''
    agent = grid[x][y]
    if agent == EMPTY:
        return True
    
    neighbors = get_neighbors(grid, x, y)
    total_neighbors = sum(1 for n in neighbors if n != EMPTY)

    if total_neighbors == 0:
        return True

    same_type_neighbors = sum(1 for n in neighbors if n == agent)
    similarity = same_type_neighbors / total_neighbors

    return similarity >= SIMILARITY_THRESHOLD

def move_unsatisfied_agents(grid):
    '''move unsatisfied ones to empties one'''
    unsatisfied = []
    empty_cells = []
    grid_size = len(grid)

    for x in range(grid_size):
        for y in range(grid_size):
            if grid[x][y] != EMPTY and not is_satisfied(grid, x, y):
                unsatisfied.append((x, y))
            elif grid[x][y] == EMPTY:
                empty_cells.append((x, y))

    if not unsatisfied or not empty_cells:
        return False

    random.shuffle(empty_cells)

    for (x, y) in unsatisfied:
        if empty_cells:
            new_x, new_y = empty_cells.pop()
            grid[new_x][new_y] = grid[x][y]
            grid[x][y] = EMPTY

    return True


def draw_grid(grid, win):
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            rect = Rectangle(Point(y * CELL_SIZE, x * CELL_SIZE), 
                             Point((y + 1) * CELL_SIZE, (x + 1) * CELL_SIZE))
            rect.setFill(COLOR_MAP[grid[x][y]])
            rect.draw(win)

def run_simulation():
    grid = initialize_grid()
    rounds = 0

    win = GraphWin("Schelling's Model", WINDOW_SIZE, WINDOW_SIZE)

    while True:
        rounds += 1
        draw_grid(grid, win)
        if not move_unsatisfied_agents(grid):
            break

    print(f"Simulation completed in {rounds} rounds.")
    win.getMouse()
    win.close()

if __name__ == "__main__":
    run_simulation()