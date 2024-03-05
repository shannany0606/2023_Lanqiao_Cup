tota=[0]*10
totb=[0]*10
ans=0
def dfs(x,ta,tb):
    global ans
    if x>7:
        if ta==0 and tb==0:ans+=1
        return
    for i in range(ta+1):
        for j in range(tb+1):
            if 2<=i+j<=5:
                tota[x]=i
                totb[x]=j
                dfs(x+1,ta-i,tb-j)
dfs(1,9,16)
print(ans)
#5067671
