#PAIR PROJECT 1: MAZE
#SAMPHASNEARYROTH CHAU (NERO) & MAYA GUPTA-LEMUS

import graphics as g
#import time #for the slow function

def draw_line(p1, p2, win):
    line = g.Line(p1, p2)
    line.setWidth(3)  # size of the line
    line.draw(win)
    #time.sleep(0.05)  # Slow down drawing

def draw_maze(maze, win):
    for y, row in enumerate(maze): #loops through the row
        for x, cell in enumerate(row): #loops through each column of the row
            if cell == "#":
                if x + 1 < len(row) and row[x + 1] == "#": #horizontal line
                    draw_line(g.Point(x, y), g.Point(x + 1, y), win)
                if y + 1 < len(maze) and maze[y + 1][x] == "#": #vertical line
                    draw_line(g.Point(x, y), g.Point(x, y + 1), win)

def main():
    with open("maze.txt") as file: 
        maze = [line.rstrip() for line in file]

    win = g.GraphWin("Maze", 400, 400)
    win.setCoords(-0.5, len(maze) - 0.5, len(maze[0]) - 0.5, -0.5)

    draw_maze(maze, win)
    win.getMouse()
    win.close()

if __name__ == "__main__":
    main()
