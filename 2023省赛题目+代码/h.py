import sys
sys.setrecursionlimit(int(1e9))
n,m=map(int,input().split())
mod=998244353
ans=0
dp={}
if m>=43:
    ans=1
    for i in range(n):
        ans*=5
        ans%=mod
    print(ans)
    sys.exit(0)
def dfs(x,n1,n2,n3,n4):
    if x>n:return 1
    Id=x*10000+n1*1000+n2*100+n3*10+n4
    if Id in dp:return dp[Id]
    tot=0
    if n4%2:
        for i in range(0,10,2):
            if n1+n2+n3+n4+i>m:break
            tot+=dfs(x+1,n2,n3,n4,i)
    else:
        for i in range(1,10,2):
            if n1+n2+n3+n4+i>m:break
            tot+=dfs(x+1,n2,n3,n4,i)
    dp[Id]=tot%mod
    return dp[Id]

for i in range(1,10,2):
    for j in range(0,10,2):
        if i+j<=m:
            for k in range(1,10,2):
                if i+j+k<=m:
                    for l in range(0,10,2):
                        if i+j+k+l<=m:
                            ans+=dfs(5,i,j,k,l)
                            if ans>mod:ans-=mod
print(ans)
