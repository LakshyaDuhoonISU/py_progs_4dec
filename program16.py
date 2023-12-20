#wap to circulate value of n variables
n=int(input("Enter number of elements: "))
list=[]
for i in range(n):
    a=int(input("Enter element: "))
    list.append(a)
print(list)
for i in range(n):
    c=list.pop(0)
    list.append(c)
    print(list)
