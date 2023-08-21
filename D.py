#D
import sys
import math
sys.setrecursionlimit(300000)
Mod=998244353
n,m=map(int,input().split())
'''
ans=1
for i in range(n-4*m):
    ans*=10
tot=0
def dfs(x,y,nw):
    global tot
    if y>m:
        tot+=1
        return
    for i in range(nw,x+1):
        dfs(x,y+1,i)
dfs(n-4*m+1,1,1)
print(n-4*m,m,tot)
print(ans*tot)
'''
def calc(x,y):
    x=x+y
    res=1
    for i in range(x,x-y,-1):
        res*=i
    for i in range(1,y+1):
        res//=i
    return res
ans=calc(n-4*m,m)
for i in range(n-4*m):
    ans=ans*10%Mod
print(ans)
