#wap to demonstrate different methods of list
#1.Create a list
l=[1,2,"abc"]
print(l)

l.append(3) #adding "3" at the end of the list
print(l)

l.extend([4,5]) #adding two elements(4,5) at the end of the list
print(l)

l.pop(2) #removing element at the index 2 in the list. By default it will remove element at the end
print(l)

l.reverse() #reversing the list
print(l)

l.remove(2) #removing element "2" in the list
print(l)

l.insert(3,2) #inserting element "2" at index 3 in the list
print(l)

l.sort(reverse=True) #sorting the list in descending order
print(l)

l.sort() #sorting the list in ascending order(only should contain elements of same data types)
print(l)