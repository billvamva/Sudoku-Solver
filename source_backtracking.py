'''
Basic Sudoku Solver using Backtracking
'''
from datetime import datetime


def print_board(arr):
    for i in range(9):
        for j in range(9):
            print(arr[i][j], end = ' ')
        print('')


def find_empty(arr, tmp):
    for row in range(9):
        for col in range(9):
            if arr[row][col] == 0:
                tmp[0] = row
                tmp[1] = col
                return True
    return False

def is_inrow(arr, row, num):
    for col in range(9):
        if arr[row][col] == num:
            return True
    return False

def is_incol(arr, col, num):
    for row in range(9):
        if arr[row][col] == num:
            return True
    return False

def is_inbox(arr, row, col, num):

    nx = (row // 3)*3
    ny = (col // 3)*3
    for i in range(nx, nx+3):
        for j in range(ny, ny+3):
            if arr[i][j] == num:
                return True

    return False

def is_safe(arr , row, col, num):
    return not is_inrow(arr, row, num) and not is_incol(arr, col, num) and not is_inbox(arr, row, col, num)

def solver(arr):

    tmp = [0,0]

    if not find_empty(arr, tmp):
        return True
    
    row = tmp[0]
    col = tmp[1]

    for i in range(1,10):

        if is_safe(arr, row, col, i):
            arr[row][col] = i

            if solver(arr):
                return True
        
            arr[row][col] = 0
    
    return False

if __name__=="__main__":
     
   
    # assigning values to the grid
    input =[[3, 0, 6, 5, 0, 8, 4, 0, 0],
          [5, 2, 0, 0, 0, 0, 0, 0, 0],
          [0, 8, 7, 0, 0, 0, 0, 3, 1],
          [0, 0, 3, 0, 1, 0, 0, 8, 0],
          [9, 0, 0, 8, 6, 3, 0, 0, 5],
          [0, 5, 0, 0, 9, 0, 6, 0, 0],
          [1, 3, 0, 0, 0, 0, 2, 5, 0],
          [0, 0, 0, 0, 0, 0, 0, 7, 4],
          [0, 0, 5, 2, 0, 6, 3, 0, 0]]
     
    # datetime module to measure run time
    start = datetime.now().microsecond
    # if success print the grid
    if(solver(input)):
        print_board(input)
    else:
        print("No solution exists")
    
    print((datetime.now().microsecond-start))