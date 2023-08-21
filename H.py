#H
import sys
sys.setrecursionlimit(300000)
n,q=map(int,input().split())
c=[0]*(n+10)
def COL(x,y,z):
    if x>n or x<1:return
    c[x]=z
    if y<=0:return
    COL(x//2,y-1,z)
    COL(x*2,y-1,z)
    COL(x*2+1,y-1,z)
while q:
    q-=1
    a=list(map(int,input().split()))
    if a[0]==1:
        COL(a[1],a[2],a[3])
    else:print(c[a[1]])
'''
6 6
1 1 1 1
2 3
1 5 2 2
2 4
2 1
2 3
'''
