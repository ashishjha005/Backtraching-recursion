def prnt(soln):
    for i in range(len(soln)):
        for j in range(len(soln)):
                print(soln[i][j],end=' ')
        print()
    print()
def ratMaze(maze,soln,x,y):
    if x==4 and y==4:
        soln[x][y]=1
        prnt(soln)
        return
    if   x>=5 or y>=5 or x<0 or y<0 or maze[x][y]==0 or soln[x][y]==1:
        return
    soln[x][y]=1
    ratMaze(maze,soln,x-1,y)
    ratMaze(maze,soln,x+1,y)
    ratMaze(maze,soln,x,y-1)
    ratMaze(maze,soln,x,y+1)
    soln[x][y]=0
maze=[[1,1,1,0,0],[1,1,0,0,1],[1,0,1,0,1],[1,1,1,1,1],[1,1,1,0,1]]
soln=[[0 for i in range(5)] for _ in range(5)]
n=5
ratMaze(maze,soln,0,0)
