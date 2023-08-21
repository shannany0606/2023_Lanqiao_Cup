#B
import sys
sys.setrecursionlimit(3000000)
sta=['1111110','0110000','1101101','1111001','0110011','1011011','1011111','1110000','1111111','1111011']
a=['0000011','1001011','0000001','0100001','0101011','0110110','1111111','0010110','0101001',
   '0010110','1011100','0100110','1010000','0010011','0001111','0101101','0110101','1101010']
b=['1011111','1110011']
def Ext(x,y):
    for i in range(7):
        if x[i]=='1' and y[i]=='0':return False
    return True
ans=1
for i in range(18):
    tot=0
    for j in range(10):
      if Ext(a[i],sta[j]):tot+=1
    ans*=tot
print(ans)
ans=1
for i in range(2):
    tot=0
    for j in range(10):
      if Ext(b[i],sta[j]):tot+=1
    ans*=tot
print(ans)
