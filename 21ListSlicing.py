'''#wap to create 2 list with odd and even numbers from a single list
list=[11,22,33,44,55]
odd=[]
even=[]
for i in range(len(list)):
    if list[i]%2==0:
        even.append(list[i])
    else:
        odd.append(list[i])
print("Original list:",list)
print("Odd numbers list:",odd)
print("Even numbers list:",even)'''

'''#wap to iterate/traverse a list in reverse order by 3 methods- 1.by reverse keyword 2.by slicing 3.by insert method
list=[10,20,30,40,50]
print("Original list:",list)
#list.reverse()
#print("Reverse list by reverse keyword:",list)
print("Reversed list using slicing:",list[::-1])'''

'''#wap to extend a list by using given approach- 1.by + operator(60,70,80) 2.by using append 3.by using extend
list=[10,20,30,40,50]
list=list+[60,70,80]
list.extend([90,100,110])
list.append(120)
print("Extended list:",list)'''

'''#wap to find sum and mean of elements in a list
list=[10,20,30,40,50]
sum=0
print("List:",list)
for i in range(len(list)):
    sum+=list[i]
print("Sum:",sum)
mean=sum/len(list)
print("Mean:",mean)'''

'''#wap to remove all duplicates from the list
list=[1,2,3,4,5,6,7,6,5,4]
list1=[]
for i in list:
    if i not in list1:
        list1.append(i)
print(list1)'''

#wap to add two matrices by using nested lists
list1=[[2,5,4],[1,3,9],[7,6,2]]
list2=[[1,8,5],[7,3,6],[4,0,9]]
result=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(list1)):
    for j in range(len(list2)):
        result[i][j]=list1[i][j]+list2[i][j]
print(result)

