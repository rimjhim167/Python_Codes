def monotone(arr):
    if(n==1):
        return 1
    else:
        return(all(arr[i]<=arr[i+1] for i in range(0,n-1)) or all(arr[i]>=arr[i+1] for i in range(0,n-1)))


arr= list()
n =int(input("enter the number of elements of the array "))
for i in range(0,n):
    arr.append(int(input("num: ")))
if(monotone(arr)):
    print("Array is monotonic")
else:
    print("Array is not monotonic")
