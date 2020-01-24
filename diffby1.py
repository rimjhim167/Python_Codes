def powof2(x):
    return (x and (not x & (x-1)))

a= int(input("1st num "))
b= int(input("2nd num "))
if(powof2(a^b) == 1):
    print("true")
else:
    print("false")