n= int(input())
l=1
r= n*n+1
print("pattern is -")
for i in range(0,n):
    for j in range(0,i):
        print("  ", end="")
    
    for j in range(i,n):
        print(str(l)+"*", end="")
        l=l+1
    
    for j in range(i,n):
        print(r, end="")
        if(j<n-1):
            print("*", end="")
        r=r+1
    r=r-((n-i)*2-1)
    print()

    
    

