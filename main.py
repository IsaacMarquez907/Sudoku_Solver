
COLUMN_COUNT = 9
ROW_COUNT = 9

sudoku_board = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
                [6, 0, 0, 1, 9, 5, 0, 0, 0],
                [0, 9, 8, 0, 0, 0, 0, 6, 0],
                [8, 0, 0, 0, 6, 0, 0, 0, 3],
                [4, 0, 0, 8, 0, 3, 0, 0, 1],
                [7, 0, 0, 0, 2, 0, 0, 0, 6],
                [0, 6, 0, 0, 0, 0, 2, 8, 0],
                [0, 0, 0, 4, 1, 9, 0, 0, 5],
                [0, 0, 0, 0, 8, 0, 0, 7, 9]]



def validate(currPos, board):

    #get current value to be tested for insertion
    currVal = board[currPos[0]][currPos[1]]

    #array showing if a number has been seen, means number has been seen, # means it has not been seen
    seenNums = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    #-----------------------------------------validate the row------------------------------------------------- 
    for i in range(ROW_COUNT):

        #if board is blank spot then keep looping
        if board[currPos[0]][i] == 0:
            continue

        
        if seenNums[board[currPos[0]][i] - 1] == 1:
            return 'invalid'
        else:
            seenNums[board[currPos[0]][i] - 1] = 1


    #-----------------------------------------validate the column------------------------------------------------- 
    seenNums = [0, 0, 0, 0, 0, 0, 0, 0, 0] #--reset the seenNums variable

    for i in range(COLUMN_COUNT):

        #if board is blank spot then keep looping
        if board[i][currPos[1]] == 0:
            continue

        
        if seenNums[board[i][currPos[1]]  - 1] == 1:
            return 'invalid'
        else:
            seenNums[board[i][currPos[1]]  - 1] = 1


    print(seenNums)













# for i in range(len(sudoku_board)):
#     for j in range(len(sudoku_board)):
#         print(sudoku_board[i][j])

cur = [8,8]
print(validate(cur, sudoku_board))
