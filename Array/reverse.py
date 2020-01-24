arr= list()
n =int(input("enter the no. of elements "))
for i in range(0,n):
    arr.append(int(input("num: ")))
for i in range(0, int(len(arr)/2)):
    t= arr[n-i-1]
    arr[n-i-1]= arr[i]
    arr[i]=t
print(arr)