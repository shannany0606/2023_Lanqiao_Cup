#I
import sys
sys.setrecursionlimit(300000)
n,p,q=map(int,input().split())
a=list(map(int,input().split()))
p-=1
q-=1
mx,mn=0,int(1e9)
for i in range(p,q+1):
    mx=max(mx,a[i])
    mn=min(mn,a[i])
ans=mx-mn
if n<=100:
    for L in range(0,p+1):
        for R in range(q,n):
            b=a.copy()
            aa=a[L:R+1]
            aa.sort()
            a=a[:L]+aa+a[R+1:]
            ans=max(ans,a[q]-a[p])
            a=b.copy()
    print(ans)
    sys.exit(0)
for L in range(0,p+1):
    R=q
    b=a.copy()
    aa=a[L:R+1]
    aa.sort()
    a=a[:L]+aa+a[R+1:]
    ans=max(ans,a[q]-a[p])
    a=b.copy()
for R in range(q,n):
    L=p
    b=a.copy()
    aa=a[L:R+1]
    aa.sort()
    a=a[:L]+aa+a[R+1:]
    ans=max(ans,a[q]-a[p])
    a=b.copy()
print(ans)

'''
5 1 4
4 5 3 3 1
'''
