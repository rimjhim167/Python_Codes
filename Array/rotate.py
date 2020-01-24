arr= list()
n= int(input("enter the number of elements "))
for i in range(0,n):
    arr.append(int(input("num: ")))
p= int(input("enter the number of times the rotation is to be done "))
l= int(input("Select   1.Left Rotation 2.Right Rotation "))
if(l==1):
    for j in range(0,p):
        t= arr[0]
        for i in range(0,n-1):
            arr[i]=arr[i+1]
        arr[n-1]=t
        print(arr)
elif(l==2):
    for j in range(0,p):
        t= arr[n-1]
        for i in range(0,n-1):
            arr[n-i-1]=arr[n-i-2]
        arr[0]=t

print(arr)