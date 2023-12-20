#wap to declare a list and print it
'''list=[10,20,30,40,50]
print("The entered list is:",list)
print("Element at index 0 is:",list[0])
print("Element at index 1 is:",list[1])
print("Element at index 2 is:",list[2])
print("Element at index 3 is:",list[3])
print("Element at index 4 is:",list[4])'''

'''list=["New Delhi","Mumbai","Pune","Nasik"]
print("The entered list is:",list)
print("Element at index 0 is:",list[0])
print("Element at index 1 is:",list[1])
print("Element at index 2 is:",list[2])
print("Element at index 3 is:",list[3])'''

'''list=["New Delhi",1,2,3,"Mumbai","Pune",4]
print("The entered list is:",list)
print("The element at index 0 is:",list[0])
print("The element at index 1 is:",list[1])
print("The element at index 2 is:",list[2])
print("The element at index 3 is:",list[3])
print("The element at index 3 is:",list[4])
print("The element at index 3 is:",list[5])
print("The element at index 3 is:",list[6])'''

#wap to perform various list operations
a=[10,20,30,40,50,60,70,80,90,100]
print("The entered list:",a)
print("First element is:",a[0])
print("Fourth element is:",a[3])
print("Elements from index 0 to index 4 are:",a[0:4])
print("Element from index -7:",a[-7])

a.append(111)
print("The entered list is:",a)

a.sort()
print("Sorted list is:",a)

a.pop()
print("List is",a)

a.remove(80)
print("List is",a)

a.insert(2,100)
print("List is",a)

print("Count of 100 is",a.count(100))

a.extend([120,130,140])
print("List is",a)

a.reverse()
print("Reversed list is",a)

