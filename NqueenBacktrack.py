def nqueen(x,r,col,d1,d2,ssf):
    if r==4:
        print(ssf)
        return
    for c in range(4):
        if d1[r+c]!=True and d2[r-c+4-1]!=True and col[c]!=True:
            x[r][c]=True
            d1[r+c]=True
            d2[r-c+4-1]=True
            col[c]= True
            nqueen(x,r+1,col,d1,d2,ssf+ str(r) + '-' +str(c) + ',')
            x[r][c]=False
            d1[r+c]=False
            d2[r-c+4-1]=False
            col[c]= False
x=[[False for i in range(4)] for _ in range(4)]
col=[False for i in range(4)]
d1=[False for i in range(2*4-1)]
d2=[False for i in range(2*4-1)]
r=0
ssf=''
nqueen(x,r,col,d1,d2,ssf)
