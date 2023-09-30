a,b,c=map(int,input().split())
if a>b:
    i=a
    a=b
    b=i
if a>c:
    i=a
    a=c
    c=i
if b>c:
    i=b
    b=c
    c=i
print(a,b,c)