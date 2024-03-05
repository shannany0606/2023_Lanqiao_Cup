n,m,a,b=map(int,input().split())
mod=998244353
S=[]
ans=0
for i in range(n):
    S.append(list(map(int,input().split())))
for i in range(n-a+1):
    mx,mn=0,int(1e9+10)
    for k in range(i,i+a):
        mx=max(mx,max(S[k][:b]))
        mn=min(mn,min(S[k][:b]))
    ans+=mx*mn
    ans%=mod
    for j in range(1,m-b+1):
        if max(S[i:i+a][j-1])==mx or min(S[i:i+a][j-1])==mn:
            mx,mn=0,int(1e9+10)
            for k in range(i,i+a):
                mx=max(mx,max(S[k][j:j+b]))
                mn=min(mn,min(S[k][j:j+b]))
        else:
            for k in range(i,i+a):mx=max(mx,S[k][j+b-1])
            for k in range(i,i+a):mn=min(mn,S[k][j+b-1])
        ans+=mx*mn
        ans%=mod
print(ans)
'''
2 3 1 2
1 2 3
4 5 6
'''
'''
10 9 5 4
2 3 3 6 6 6 7 8 9
1 9 2 6 5 8 1 7 6
2 4 5 7 7 1 3 8 5
5 3 8 7 3 9 5 7 2
3 8 4 7 6 5 2 4 6
2 3 3 6 6 6 7 8 9
1 9 2 6 5 8 1 7 6
2 4 5 7 7 1 3 8 5
5 3 8 7 3 9 5 7 2
3 8 4 7 6 5 2 4 6
'''
