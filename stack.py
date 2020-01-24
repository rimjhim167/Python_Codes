stack= []
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)

print("Stack- ")
print(stack)

if(len(stack)):
    print("Top item is "+ str(stack.pop()))

print("Stack after pop- ")
print(stack)