#wap that creates a list of 10 random integers
#wap to print index at which a particular value exists. if the value exists at multiple locations in the list, then print all the indices. also count number of times the value is repeated in the list.
n=int(input("Enter number of elements: "))
list=[]
count=0
for i in range(n):
    a=int(input("Enter element: "))
    list.append(a)
print(list)
b=int(input("Enter element to search for: "))
for i in range(n):
    if list[i]==b:
        count+=1
        print(b,"found at index",i)
print(b,"found",count,"times")
