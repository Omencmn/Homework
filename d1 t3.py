def fibonacci(n):
    s=0
    if(n==1):
        return 0
    elif(n==2):
        return 1
    else:
        s+=fibonacci(n-1)+fibonacci(n-2)
        n-=1
    return s
#稍加改造可以实现自动化输入
for i in range (1,21):
    print(fibonacci(i)," ")
