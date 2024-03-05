n=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
C=list(map(int,input().split()))
D=[]
for i in range(n):
    D.append((A[i],B[i],C[i]))
ans=0
D.sort(key=lambda x:-(x[0]-x[1]-x[2]))
#print(D)
sum=0
for i in range(n):
    sum+=D[i][0]-D[i][1]-D[i][2]
    if sum<=0:
        ans=max(ans,i)
        break

D.sort(key=lambda x:-(x[1]-x[0]-x[2]))
#print(D)
sum=0
for i in range(n):
    sum+=D[i][1]-D[i][0]-D[i][2]
    if sum<=0:
        ans=max(ans,i)
        break

D.sort(key=lambda x:-(x[2]-x[0]-x[1]))
#print(D)
sum=0
for i in range(n):
    sum+=D[i][2]-D[i][0]-D[i][1]
    if sum<=0:
        ans=max(ans,i)
        break
if ans:print(ans)
else:print(-1)
'''
3
1 2 2
2 3 2
1 0 7
'''
