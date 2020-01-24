arr= list()
n= int(input("enter the no. of elements "))
for i in range(0,n):
    arr.append(int(input("num: ")))
s=0
for i in arr:
    s=s+i
print(s)