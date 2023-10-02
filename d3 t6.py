a=int(input("请输入年:"))
b=int(input("请输入月:"))
c=int(input("请输入日:"))
def judge(a):
    if (a%4==0 and a%100!=0):
        return 1
    elif a%400==0:
        return 1
    else:
        return 0

s=c
for i in range(1,b):
    if i==1 or i==3 or i==5 or i==7 or i==8 or i==10 or i==12:
        s+=31
    elif i==2:
        s+=28
    else:
        s+=30
if(judge(a)==1 and b>2):
    s+=1
print(f"为该年第{s}天")