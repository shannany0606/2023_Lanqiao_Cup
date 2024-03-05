n=int(input())
A=list(map(int,input().split()))
ans=min(A)+1
data={}
for i in A:
    if i in data:data[i]+=1
    else:data[i]=1
while 1:
    num=data[ans-1]
    if num%ans!=0:
        ans-=1
        break
    if ans in data:data[ans]+=num//ans
    else:data[ans]=num//ans
    ans+=1
print(ans)
    
