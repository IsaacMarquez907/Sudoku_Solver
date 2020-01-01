import unittest
import objects
import main

class TestSudokuSolver(unittest.TestCase):

    #test the cell class, that is works properlly
    def test_cell(self):
        #create cell object
        c1 = objects.cell([2,4])

        #test initialization is correct
        self.assertEqual(c1.currPos, [2,4])
        self.assertEqual(c1.triedValues, [0,0,0,0,0,0,0,0,0])


    #test the validate function
    def test_validate(self):
        #test that it finds errors in 9 x 9 sudoku board
        #error in row 0,4 and 9. As well as column 0, 4 and 9
        COLUMN_COUNT = 9
        ROW_COUNT = 9

        sudoku_board = [[7, 3, 0, 0, 7, 0, 0, 0, 0],
                        [6, 0, 0, 1, 9, 5, 0, 0, 0],
                        [0, 9, 8, 0, 0, 0, 0, 6, 0],
                        [8, 0, 0, 0, 1, 0, 0, 0, 3],
                        [4, 0, 0, 8, 0, 3, 0, 0, 1],
                        [7, 0, 0, 0, 2, 0, 0, 0, 6],
                        [0, 6, 0, 0, 0, 0, 2, 8, 0],
                        [0, 0, 0, 4, 1, 9, 0, 0, 5],
                        [0, 0, 0, 0, 8, 0, 0, 7, 3]]

        curr = objects.cell([0,0])
        self.assertEqual(main.validate(curr, sudoku_board), False)

        curr = objects.cell([4,4])
        self.assertEqual(main.validate(curr, sudoku_board), False)

        curr = objects.cell([8,8])
        self.assertEqual(main.validate(curr, sudoku_board), False)

        curr = objects.cell([2,2])
        self.assertEqual(main.validate(curr, sudoku_board), True)

        curr = objects.cell([7,7])
        self.assertEqual(main.validate(curr, sudoku_board), True)




if __name__ == '__main__':
    unittest.main()
