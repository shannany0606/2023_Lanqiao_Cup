n=int(input())
A=[]
tot=[0]*15
gg=[0]*(n+10)
for i in range(n):
    x,y=map(int,input().split())
    A.append((y,x))
A.sort(key=lambda x:-x[0])
lim=n//10
ans=0
for i in range(n):
    if tot[A[i][1]]<lim:tot[A[i][1]]+=1
    else:ans+=A[i][0]
print(ans)
'''
10
1 1
1 2
1 3
2 4
2 5
2 6
3 7
3 8
3 9
4 10
'''
