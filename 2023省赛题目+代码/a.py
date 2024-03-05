def run(x):
    if x%4==0 and x%100!=0:return 1
    if x%400==0:return 1
    return 0
ans=0
lim=[0,31,30,31,30,31,30,31,31,30,31,30,31]
for i in range(2000,2000000):
    if run(i):lim[2]=29
    else:lim[2]=28
    for j in range(1,13):
        for k in range(1,lim[j]+1):
            if i%j==0 and i%k==0:ans+=1
print(ans+1)
#35813063
