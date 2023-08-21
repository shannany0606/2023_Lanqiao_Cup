#G
import sys
sys.setrecursionlimit(300000)
n=int(input())
num={}
a=list(map(int,input().split()))
S=sum(a)
for i in range(n):
    if a[i] in num:num[a[i]]+=1
    else:num[a[i]]=1
dat=[]
for x,c in num.items():
    dat.append((c,x))
dat.sort(key=lambda x:-x[0])
#print(dat)
m=len(dat)
if m==1 or m==2:
    print(0)
    sys.exit(0)
ans=int(1e18)
mx=dat[0][0]
for i in range(min(150,m)):
    base=dat[i][1]
    avg=(S-dat[i][1]*dat[i][0])//(n-dat[i][0])
    nw=avg+1
    if nw>=2*base:nw=2*base-1
    if base>=2*nw:nw=base//2+1
    tot=0
    for j in range(m):
        if i!=j:tot+=abs(nw-dat[j][1])*dat[j][0]
    #print(base,avg+1,tot)
    ans=min(ans,tot)
    nw=avg
    if nw>=2*base:nw=2*base-1
    if base>=2*nw:nw=base//2+1
    tot=0
    for j in range(m):
        if i!=j:tot+=abs(nw-dat[j][1])*dat[j][0]
    #print(base,avg+1,tot)
    ans=min(ans,tot)
print(ans)
    
