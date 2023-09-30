flag=0
for i in range(101,201):
    for j in range(2,i):
        if(i%j==0):
            flag=1
            break
    if(flag==0):
        print(i,end=' ')
    flag=0