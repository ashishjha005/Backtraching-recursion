def helper(sudoku,po,x,y):
    for i in range(9):
        if sudoku[x][i]==po:
            return False
    for i in range(9):
        if sudoku[i][y]==po:
            return False
    nis=3*(x//3)
    njs=3*(y//3)
    for i in range(3):
        for j in range(3):
            if sudoku[nis+i][njs+j]==po:
                return False
    return True

def sudokusolver(sudoku,i,j):
    if i==9:
        print(*sudoku)
        return
    nj=0
    ni=0
    if j<8:
        nj=j+1
        ni=i
    else:
        ni=i+1
        nj=0
    if sudoku[i][j]!=0:
        sudokusolver(sudoku,ni,nj)
    else:
      for po in range(1,10):
        if sudoku[i][j]==0:
            if helper(sudoku,po,i,j):
             sudoku[i][j]=po
             sudokusolver(sudoku,ni,nj)
             sudoku[i][j]=0
            
    
sudoku= [[3,0,6,5,0,8,4,0,0],
 [5,2,0,0,0,0,0,0,0],
 [0,8,7,0,0,0,0,3,1],
 [0,0,3,0,1,0,0,8,0],
 [9,0,0,8,6,3,0,0,5],
 [0,5,0,0,9,0,6,0,0],
 [1,3,0,0,0,0,2,5,0],
 [0,0,0,0,0,0,0,7,4],
 [0,0,5,2,0,6,3,0,0]]
sudokusolver(sudoku,0,0)
