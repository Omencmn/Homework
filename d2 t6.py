#C++训练好像也有？按我当时思路来做了
def judge(n):
    flag=0
    for i in range(2,n):
        if (n%i==0):
            flag = 1
            break
    if (flag == 0):
        return 1
    else:
        return 0
m=int(input("请输入需要分解的数字:"))
print(f"{m}=",end='')
k=m
if(judge(m)):
    print("此数为质数，不用分解")
else:
    for i in range (2,k+1):
        if((judge(i))==1 and m!=i):
            while ((m % i)== 0):
                m=int(m/i)
                print(f"{i}*",end='')
        elif (m==i):
            print(m,end='')
            break