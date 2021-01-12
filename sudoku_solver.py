def find_empty(brd):
    """Identifies 1st missing position on provided sudoku board.

    Args:
        brd (list): Sudoku board, a list of lists

    Returns:
        tuple: Tuple of row and column index
    """

    # missing values marked by 0
    for i, row in enumerate(brd, start=0):
        for ii, value in enumerate(row, start=0):
            if value == 0:
                # return row and col
                return (i, ii)
    return None

def possible(brd, num, pos):
    """Checks whether the value in range from 1 to 9 is suitable
       for this position under sudoku rules. 

    Args:
        brd (list): Sudoku board, a list of lists
        num (int): Value for evaluation
        pos (tuple): row and column positions

    Returns:
        bool: True or False
    """

    # first, check row
    for i in range(0,9):
        if brd[pos[0]][i] == num and pos[1] != i:
            return False
    
    # second, check col
    for i in range(0,9):
        if brd[i][pos[1]] == num and pos[0] != i:
            return False

    # third, check 3 by 3 box
    box_x = (pos[1] // 3) * 3
    box_y = (pos[0] // 3) * 3

    for i in range(box_y, box_y + 3):
        for ii in range(box_x, box_x + 3):
            if brd[i][ii] == num and (i, ii) != pos:
                return False

    return True

def solver(brd):
    """Solves provided sudoku board.

    Args:
        brd (list): An unsolved sudoku board, a list of lists

    Returns:
        bool: True or False
    """

    # find first empty position on board
    missing_pos = find_empty(brd)
    if not missing_pos:
        return True
    else:
        row, col = missing_pos

    for i in range(1,10):
        # check if i value is possible in this position
        if possible(brd, i, (row, col)):
            brd[row][col] = i

            # recursively call solver
            if solver(brd):
                return True

            brd[row][col] = 0
    
    # Puzzle may not be always valid
    return False

def board_return(brd):
    """Prints sudoku board in a nice and clear format.

    Args:
        brd (list): Sudoku board, a list of lists
    """

    for i, row in enumerate(brd, start=0):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
        
        for ii, value in enumerate(row, start=0):
            if ii % 3 == 0 and ii != 0:
                print(" | ", end="")
            
            if ii == 8:
                print(value)
            else:
                print(str(value) + " ", end="")

# example
if __name__ == '__main__':
    example_grid = [
    [0,2,0,0,0,0,0,0,0],
    [0,0,0,6,0,0,0,0,3],
    [0,7,4,0,8,0,0,0,0],
    [0,0,0,0,0,3,0,0,2],
    [0,8,0,0,4,0,0,1,0],
    [6,0,0,5,0,0,0,0,0],
    [0,0,0,0,1,0,7,8,0],
    [5,0,0,0,0,9,0,0,0],
    [0,0,0,0,0,0,0,4,0]
    ]

    import time
    print("Example board:")
    board_return(example_grid)
    start_time = time.time()
    solver(example_grid)
    print("Solved board:")
    board_return(example_grid)
    print(f"Took us {time.time() - start_time} seconds!")