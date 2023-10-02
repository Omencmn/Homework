str="*"
for i in range(1,5):
    for j in range (1,5-i):
        print(" ",end='')
    for j in range (1,2*i):
        print(str,end='')
    print()
for i in range (1,4):
    for j in range(1,i+1):
        print(" ",end='')
    for j in range(1,8-2*i):
        print(str,end='')
    print()