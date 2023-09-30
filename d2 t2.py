a=int(input("请输入a的值:"))
n=int(input("请输入几个数相加:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(a,end='')
    print("+",end='')
print("=",end='')
sum=0
for i in range(1,n+1):
    sum+=a
    a*=11
print(sum,end='')