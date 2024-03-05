Q=int(input())
for _ in range(Q):
    T=list(input())
    S=list(input())
    n=len(T)
    if S[0]!=T[0] or S[n-1]!=T[n-1]:
        print(-1)
        continue
    ans=0
    flag=1
    gg=1
    while flag and gg:
        flag=0
        gg=0
        for i in range(1,n-1):
            if S[i]!=T[i]:
                if S[i]!=S[i-1] and S[i]!=S[i+1]:
                    S[i]=S[i-1]
                    flag=1
                    ans+=1
                else:gg=1
    if gg:print(-1)
    else:print(ans)
'''
2
1000111
1010101
01000
11000
'''
