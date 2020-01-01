import objects


def validate(currCell, board):

    #get current value to be tested for insertion
    currVal = board[currCell.currPos[0]][currCell.currPos[1]]

    #array showing if a number has been seen, means number has been seen, # means it has not been seen
    seenNums = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    #-----------------------------------------validate the row------------------------------------------------- 
    for i in range(ROW_COUNT):

        #if board is blank spot then keep looping
        if board[currCell.currPos[0]][i] == 0:
            continue

        
        if seenNums[board[currCell.currPos[0]][i] - 1] == 1:
            return False
        else:
            seenNums[board[currCell.currPos[0]][i] - 1] = 1


    #-----------------------------------------validate the column------------------------------------------------- 
    seenNums = [0, 0, 0, 0, 0, 0, 0, 0, 0] #--reset the seenNums variable

    for i in range(COLUMN_COUNT):

        #if board is blank spot then keep looping
        if board[i][currCell.currPos[1]] == 0:
            continue

        
        if seenNums[board[i][currCell.currPos[1]]  - 1] == 1:
            return False
        else:
            seenNums[board[i][currCell.currPos[1]]  - 1] = 1


    #-----------------------------------------validate the subBox------------------------------------------------- 
    seenNums = [0, 0, 0, 0, 0, 0, 0, 0, 0] #--reset the seenNums variable






    #returns true if hasn't found any errors
    return True



