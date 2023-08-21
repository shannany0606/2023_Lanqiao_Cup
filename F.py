#F
import sys
sys.setrecursionlimit(300000)
n=int(input())
h=[]
for i in range(n):
    a=list(map(int,input().split()))
    h.append(a)
PP=[[(0,0)]*(n+10) for i in range(n+10)]
MM=[[(0,0)]*(n+10) for i in range(n+10)]
for r in range(n):
    for c in range(n):
        cc=c
        while cc+1<n and h[r][cc+1]<h[r][cc]:
            cc+=1
        PP[r][c]=(r,cc)
        cc=c
        while cc-1>=0 and h[r][cc-1]<h[r][cc]:
            cc-=1
        MM[r][c]=(r,cc)
Q=[(0,0,0)]
vis=set()
st,ed=0,0
while st<=ed:
    r=Q[st][0]
    c=Q[st][1]
    t=Q[st][2]
    st+=1
    if r==n-1 and c==n-1:
        print(t)
        #print(Q)
        sys.exit(0)
    if r+1<n:
        if (r+1,c) not in vis:
            Q.append((r+1,c,t+1))
            ed+=1
            vis.add((r+1,c))
    if c+1<n:
        if (r,c+1) not in vis:
            Q.append((r,c+1,t+1))
            ed+=1
            vis.add((r,c+1))
    P=PP[r][c]
    if P!=(r,c) and P!=(r,c+1):
        if (r,P[1]) not in vis:
            Q.append((r,P[1],t+1))
            ed+=1
            vis.add((r,P[1]))
    M=MM[r][c]
    if M!=(r,c):
        if (r,M[1]) not in vis:
            Q.append((r,M[1],t+1))
            ed+=1
            vis.add((r,M[1]))
'''
4
0 1 9 3
2 9 3 7
8 4 8 9
9 8 0 7
'''
