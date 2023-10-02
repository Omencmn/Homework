a=int(input())
s=0
o=a
while(a!=0):
    a//=10
    s+=1
print(f"该数为{s}位数")
k=str(o)
print("各位数字为:",end='')
for i in k:
    print(i,end=' ')