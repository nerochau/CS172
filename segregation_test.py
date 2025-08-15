#SAMPHASNEARYROTH CHAU & MAYA GUPTA-LEMUS
 
import unittest
from segregation import initialize_grid, get_neighbors, is_satisfied, move_unsatisfied_agents, EMPTY, RED, BLUE

class TestSchellingModel(unittest.TestCase):

    def test_initialize_grid(self):
        """Test if the grid initializes correctly with the right proportions."""
        grid = initialize_grid()
        red_count = sum(row.count(RED) for row in grid)
        blue_count = sum(row.count(BLUE) for row in grid)
        empty_count = sum(row.count(EMPTY) for row in grid)
        total_cells = len(grid) * len(grid[0])

        expected_empty = int(total_cells * 0.1)  # EMPTY_RATIO
        expected_red = (total_cells - expected_empty) // 2
        expected_blue = total_cells - expected_empty - expected_red

        self.assertEqual(red_count, expected_red)
        self.assertEqual(blue_count, expected_blue)
        self.assertEqual(empty_count, expected_empty)

    def test_get_neighbors(self):
        """Test if the function correctly finds neighbors for a given cell."""
        grid = [
            [RED, BLUE, RED],
            [BLUE, EMPTY, RED],
            [RED, BLUE, RED]
        ]
        neighbors = get_neighbors(grid, 1, 1)  # Checking neighbors of the center cell
        self.assertEqual(len(neighbors), 8)
        self.assertIn(RED, neighbors)
        self.assertIn(BLUE, neighbors)

    def test_is_satisfied(self):
        grid = [
            [RED, BLUE, RED],
            [BLUE, RED, BLUE],
            [RED, BLUE, RED]
        ]
        self.assertTrue(is_satisfied(grid, 1, 1))

        grid[1][1] = BLUE
        self.assertTrue(is_satisfied(grid, 1, 1))

        grid = [
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, RED, EMPTY],
            [EMPTY, EMPTY, EMPTY]
        ]
        self.assertTrue(is_satisfied(grid, 1, 1))



    def test_move_unsatisfied_agents(self):
        """Test if unsatisfied agents are moved to empty cells."""
        grid = [
            [RED, BLUE, RED],
            [BLUE, RED, EMPTY],
            [RED, BLUE, RED]
        ]
        moved = move_unsatisfied_agents(grid)
        self.assertTrue(moved)  # Since there's an empty cell, a move should happen
        self.assertEqual(sum(row.count(EMPTY) for row in grid), 1)  # Still one empty cell

if __name__ == '__main__':
    unittest.main()