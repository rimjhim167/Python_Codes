n =int(input())
l=[]
for i in range(n):
    l.append(int(input()))
print(l)
for i in range(0, 1<<n):
    for j in range(0, n):
        if((i & (1<<j))>0):
            print(l[j], end=',')
        
    print("")