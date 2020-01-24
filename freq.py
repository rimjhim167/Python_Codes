import operator
f={}
def freq(l):
    
    for li in l:
        if(li in f):
            f[li]+=1
        else:
            f[li]=1
    return f

n=int(input("enter no of elements"))
l=[]
for i in range(0,n):
    l.append(int(input()))
print(freq(l))

print(sorted(f.items(), key=operator.itemgetter(1), reverse=True))
