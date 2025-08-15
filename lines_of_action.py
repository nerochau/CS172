#SAMPHASNEARYROTH CHAU (NERO) & MAYA GUPTA-LEMUS
 
from graphics import *

CELL_SIZE = 50
EMPTY, BLACK, WHITE = 0, 1, 2

class Vector:
    def __init__(self, dx, dy):
        self.dx = dx
        self.dy = dy

    def __add__(self, o):
        return Vector(self.dx + o.dx, self.dy + o.dy)

    def __mul__(self, s):
        return Vector(self.dx * s, self.dy * s)

    def __eq__(self, o):
        return self.dx == o.dx and self.dy == o.dy

# the game board
class Board:
    def __init__(self, win, size=8):
        self.win = win 
        self.size = size  
        self.grid = [[EMPTY]*size for _ in range(size)]  # piece state
        self.squares = [[None]*size for _ in range(size)]  # square visual
        self.pieces = [[None]*size for _ in range(size)]  # piece visual
        self.selected = None  # currently selected one
        self.highlights = []  # possible move

        # setting up init position of the piece
        for i in range(1, size-1):
            self.grid[0][i] = BLACK
            self.grid[size-1][i] = BLACK
            self.grid[i][0] = WHITE
            self.grid[i][size-1] = WHITE
        self.draw_board()
        self.draw_pieces()

    def in_bounds(self, r, c):
        return 0 <= r < self.size and 0 <= c < self.size

    def get(self, r, c):
        return self.grid[r][c]

    def draw_board(self):
        for r in range(self.size):
            for c in range(self.size):
                x, y = c * CELL_SIZE, r * CELL_SIZE
                rect = Rectangle(Point(x, y), Point(x + CELL_SIZE, y + CELL_SIZE))
                rect.setOutline("black")
                rect.draw(self.win)
                self.squares[r][c] = rect

    def draw_pieces(self):
        # Draw the pieces (black and white) on the board
        for r in range(self.size):
            for c in range(self.size):
                if self.pieces[r][c]:
                    self.pieces[r][c].undraw()  # remove exisitng piece
                    self.pieces[r][c] = None
                if self.grid[r][c] != EMPTY:
                    color = "black" if self.grid[r][c] == BLACK else "white"
                    circle = Circle(Point(c * CELL_SIZE + 25, r * CELL_SIZE + 25), 20)
                    circle.setFill(color)
                    circle.draw(self.win)
                    self.pieces[r][c] = circle

    def move(self, fr, to):
        # when piece move from one to another
        self.grid[to[0]][to[1]] = self.grid[fr[0]][fr[1]]
        self.grid[fr[0]][fr[1]] = EMPTY
        self.draw_pieces()  # need to redraw once moved

    def clear_highlights(self):
        # remove the highlight
        for r, c in self.highlights:
            self.squares[r][c].setWidth(1)
            self.squares[r][c].setOutline("black")
        if self.selected:
            r, c = self.selected
            self.squares[r][c].setWidth(1)
            self.squares[r][c].setOutline("black")
        self.highlights = []

    def highlight_moves(self, r, c, moves):
        # highlight possible move of the chosen piece
        self.squares[r][c].setOutline("blue")
        self.squares[r][c].setWidth(3)
        for mr, mc in moves:
            self.squares[mr][mc].setOutline("green")
            self.squares[mr][mc].setWidth(3)
        self.selected = (r, c)
        self.highlights = moves

    def count_line(self, r, c, d):
        # count number of piece in the same direction
        count = 1 if self.grid[r][c] != EMPTY else 0
        for s in [1, -1]:
            rr, cc = r + s * d.dx, c + s * d.dy
            while self.in_bounds(rr, cc):
                if self.grid[rr][cc] != EMPTY:
                    count += 1
                rr += s * d.dx
                cc += s * d.dy
        return count

    def legal_moves(self, r, c):
        # get the legal move for a piece at (r, c)
        if not self.in_bounds(r, c) or self.grid[r][c] == EMPTY:
            return []
        color = self.grid[r][c]
        dirs = [Vector(dr, dc) for dr in [-1, 0, 1] for dc in [-1, 0, 1] if dr or dc]
        moves = []
        for d in dirs:
            dist = self.count_line(r, c, d)
            rr, cc = r + d.dx * dist, c + d.dy * dist
            if not self.in_bounds(rr, cc): continue
            # check to not go over enemy
            blocked = False
            for step in range(1, dist):
                tr, tc = r + d.dx * step, c + d.dy * step
                if self.in_bounds(tr, tc) and self.grid[tr][tc] not in [EMPTY, color]:
                    blocked = True
                    break
            if not blocked and self.grid[rr][cc] != color:
                moves.append((rr, cc))
        return moves

    def all_pieces_connected(self, color):
        # connected or not
        visited = set()

        # depth-first search
        def dfs(r, c):
            if (r, c) in visited: return
            visited.add((r, c))
            for d in [Vector(dr, dc) for dr in [-1, 0, 1] for dc in [-1, 0, 1] if dr or dc]:
                nr, nc = r + d.dx, c + d.dy
                if self.in_bounds(nr, nc) and self.grid[nr][nc] == color:
                    dfs(nr, nc)

        for r in range(self.size):
            for c in range(self.size):
                if self.grid[r][c] == color:
                    dfs(r, c)
                    return sum(row.count(color) for row in self.grid) == len(visited)
        return False

# Function to translate mouse click into board coordinates
def get_clicked_square(p):
    return int(p.getY() // CELL_SIZE), int(p.getX() // CELL_SIZE)

# to run the game
def main():
    win = GraphWin("Lines of Action", CELL_SIZE * 8, CELL_SIZE * 8) #window
    board = Board(win)  # init board
    current_player = BLACK  # black start first

    while True:
        pt = win.getMouse()
        r, c = get_clicked_square(pt)

        if board.selected and (r, c) in board.highlights:
            # Move piece if selected and the square is a legal move
            board.move(board.selected, (r, c))
            if board.all_pieces_connected(current_player):
                # check if current player win
                msg = Text(Point(CELL_SIZE * 4, CELL_SIZE * 4), f"{'Black' if current_player == BLACK else 'White'} wins!")
                msg.setSize(18)
                msg.setStyle("bold")
                msg.setTextColor("red")
                msg.draw(win)
                break  # exit game loop
            current_player = WHITE if current_player == BLACK else BLACK  # switch player
            board.clear_highlights()  # clear the highlights
            board.selected = None  # deselect
        elif board.in_bounds(r, c) and board.get(r, c) == current_player:
            # select and show legal move
            board.clear_highlights()
            moves = board.legal_moves(r, c)
            board.highlight_moves(r, c, moves)
        else:
            # deselect if no legal move
            board.clear_highlights()
            board.selected = None

    win.getMouse()
    win.close() 

if __name__ == "__main__":
    main()
