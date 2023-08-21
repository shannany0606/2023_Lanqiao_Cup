#C
import sys
sys.setrecursionlimit(300000)
x=int(input())
ans=0
while x:
    ans+=1
    xx=x
    xx=list(str(xx))
    xx=map(int,xx)
    x-=sum(xx)
print(ans)
    
