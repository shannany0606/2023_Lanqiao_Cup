#E
import sys
import math
sys.setrecursionlimit(300000)
Mod=998244353
n,A,B=map(int,input().split())
a=list(map(int,input().split()))
dp=set()
dp.add((0,0))
dat=[]
for i in range(n):
    for x in dp:
        xx,yy=x[0]+a[i],x[1]
        if xx<=A and yy<=B:dat.append((xx,yy))
        xx,yy=x[0],x[1]+a[i]
        if xx<=A and yy<=B:dat.append((xx,yy))
    for x in dat:
        dp.add(x)
    dat.clear()
ans=0
for x in dp:
    ans=max(ans,x[0]+x[1])
print(ans)
