#wap to find smallest and largest number in a list
n=int(input("Enter number of elements: "))
list=[]
for i in range(n):
    a=int(input("Enter element: "))
    list.append(a)
print(list)
'''list.sort()
print("Smallest number:",list[0])
print("Largest number:",list[n-1])
'''
for i in range(len(list)-1):
    for j in range(len(list)-1-i):
        if list[j]>list[j+1]:
            temp=list[j]
            list[j]=list[j+1]
            list[j+1]=temp
print("Smallest number:",list[0])
print("Largest number:",list[n-1])

'''max=list[0]
for i in range(len(list)):
    if max<list[i]:
        max=list[i]
min=list[0]
for i in range(len(list)):
    if min>list[i]:
        min=list[i]
print(max)
print(min)'''
