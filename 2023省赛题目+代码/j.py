s=input()
n=len(s)
ans=0
for c in s:
    if c=='1':ans+=1
tot=ans
for i in range(n):
    if s[i]=='0':
        mv=1
        cnt=0
        while 0<=i-mv<=n-1 and 0<=i+mv<=n-1:
            if s[i-mv]!=s[i+mv]:
                mv-=1
                break
            if s[i+mv]=='1':cnt+=1
            mv+=1
        ans=min(ans,tot-cnt)
for i in range(n-1):
    if s[i]==s[i+1]:
        mv=1
        if s[i]=='1':cnt=1
        else:cnt=0
        while 0<=i-mv<=n-1 and 0<=i+1+mv<=n-1:
            if s[i-mv]!=s[i+mv]:
                mv-=1
                break
            if s[i-mv]=='1':cnt+=1
            mv+=1
        ans=min(ans,tot-cnt)
print(ans)
'''
00111011
'''
