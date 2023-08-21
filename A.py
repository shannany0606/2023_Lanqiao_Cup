#A
import sys
sys.setrecursionlimit(3000000)
mon=[0,31,28,31,30,31,30,31,31,30,31,30,31]
nw=0
ans=0
def check(x):
    while x:
        if x%10==1:return True
        x=x//10
    return False
for i in range(1,13):
    for j in range(1,mon[i]+1):
        if nw==1 or check(i) or check(j):
            ans+=5
            print(i,j,nw,5)
        else:
            ans+=1
            print(i,j,nw,1)
        nw=(nw+1)%7      
print(ans)
