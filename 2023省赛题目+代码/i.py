def calc(num,tot,nw,n,m,k):
    ans=1
    L=1
    while tot<=n:
        nw*=m
        num*=m
        L*=m
        st,ed=tot+num+1,tot+num+L
        #print(st,ed)
        if ed<=n:ans+=L
        elif st>n:return ans
        else:return ans+n-st+1
        tot+=nw
    return 0
T=int(input())
for _ in range(T):
    n,m,k=map(int,input().split())
    tot,nw,i=0,1,0
    while tot<n:
        if i:nw*=m
        tot+=nw
        if tot>=n:
            print(1)
            break
        if k<=tot:
            if tot+nw*m<=n:
                print(calc(k-(tot-nw)-1,tot,nw,n,m,k))
                break
            else:
                num=k-(tot-nw)-1
                gu=tot+num*m
                if gu>=n:
                    print(1)
                    break
                if gu+m<=n:
                    print(m+1)
                    break
                print(n-gu+1)
                break
        i+=1
'''
3
1 2 1
11 3 4
74 5 3
'''
