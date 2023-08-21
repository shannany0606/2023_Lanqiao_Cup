#J
import sys
sys.setrecursionlimit(300000)
S=input()
T=input()
n,m=len(S),len(T)
ans=0
tran={}
for i in range(n):
    for j in range(m):
        k=0
        tran.clear()
        while i+k<n and j+k<m:
            if S[i+k] not in tran:
                tran[S[i+k]]=T[j+k]
            elif tran[S[i+k]]!=T[j+k]:
                break
            k+=1
        ans=max(ans,k)
print(ans)
'''
aaaba
yxyy
'''
