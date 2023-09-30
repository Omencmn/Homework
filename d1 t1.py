s=0
for i in range(1,5):
    for j in range(1,5):
        for p in range(1,5):
            if (i!=j)&(j!=p)&(p!=i):
                s+=1
print(s)