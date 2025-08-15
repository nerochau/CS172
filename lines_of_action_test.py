#SAMPHASNEARYROTH CHAU (NERO) & MAYA GUPTA-LEMUS

import unittest
from graphics import GraphWin
from lines_of_action import Board, EMPTY, BLACK, WHITE

class TestBoard(unittest.TestCase):
    def setUp(self):
        """Set up a new board for testing."""
        self.win = GraphWin("Test", 400, 400)
        self.board = Board(self.win)

    def test_initial_grid(self):
        """Test the initial state of the board."""
        for i in range(1, self.board.size - 1):
            self.assertEqual(self.board.get(0, i), BLACK) 
            self.assertEqual(self.board.get(self.board.size - 1, i), BLACK)
            self.assertEqual(self.board.get(i, 0), WHITE) 
            self.assertEqual(self.board.get(i, self.board.size - 1), WHITE)

        for r in range(1, self.board.size - 1):
            for c in range(1, self.board.size - 1):
                self.assertEqual(self.board.get(r, c), EMPTY)

    def test_move(self):
        """Test that a piece moves correctly from one square to another."""
        self.board.grid[1][1] = BLACK
        self.board.move((1, 1), (2, 2))
        self.assertEqual(self.board.get(2, 2), BLACK)
        self.assertEqual(self.board.get(1, 1), EMPTY)

    def test_legal_moves(self):
        """Test the legal moves for a specific piece."""
        r, c = 1, 1
        self.board.grid[r][c] = BLACK

        moves = self.board.legal_moves(r, c)

        self.assertTrue(len(moves) > 0)

    def test_illegal_move(self):
        """Test that an illegal move is correctly prevented."""
        self.board.grid[1][1] = BLACK
        self.board.grid[2][2] = WHITE 
        legal_moves = self.board.legal_moves(1, 1)
        self.assertNotIn((2, 2), legal_moves)

    def test_highlight_moves(self):
        """Test that valid moves are highlighted correctly."""
        self.board.grid[1][1] = BLACK
        moves = self.board.legal_moves(1, 1)
        
        self.board.highlight_moves(1, 1, moves)
        
        self.assertEqual(self.board.squares[1][1].config['outline'], "blue")
        for r, c in moves:
            self.assertEqual(self.board.squares[r][c].config['outline'], "green")

    def test_win_condition(self):
        """Test if the win condition for a player is correctly detected."""
        self.board.grid = [[EMPTY]*8 for _ in range(8)] 
        self.board.grid[0][1] = BLACK
        self.board.grid[1][1] = BLACK
        self.board.grid[1][2] = BLACK
        self.board.grid[2][1] = BLACK

        self.assertTrue(self.board.all_pieces_connected(BLACK))

        self.board.move((2, 1), (2, 2))
        self.assertTrue(self.board.all_pieces_connected(BLACK)) 

    def tearDown(self):
        """Close the window after testing."""
        self.win.close()

if __name__ == "__main__":
    unittest.main()
