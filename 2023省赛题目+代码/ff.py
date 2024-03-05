n,m,a,b=map(int,input().split())
mod=998244353
S=[]
ans=0
for i in range(n):
    S.append(list(map(int,input().split())))
for i in range(n-a+1):
    for j in range(m-b+1):
        mx,mn=0,int(1e9+10)
        for k in range(i,i+a):
            mx=max(mx,max(S[k][j:j+b]))
            mn=min(mn,min(S[k][j:j+b]))
        ans+=mx*mn
        ans%=mod
print(ans)
