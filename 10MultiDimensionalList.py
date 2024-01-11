#multi dimensional list
my2DList=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print(my2DList)
print(my2DList[2][0])

my2DList=[[1,2,3,"4"],[5,6,"7",8],["a",10,11,12],[13,"14",15,16]] #nested list can have elements of different data types
print(my2DList)
print(my2DList[2][0])

my2DList=[[1,2,3,4],[7,8],[9,10,11],[14,15,16]] #nested list can be of different length
print(my2DList)
print(my2DList[2][0])
print(my2DList[2])
print(len(my2DList)) #length of my2DList
print(len(my2DList[2])) #length of list at index 2 of my2DList

sub=[["p","q"],["r","s"]]
my2DList=[[1,2,3,"4"],[5,6,"7",8],["a",10,11,12],[13,"14",15,sub]]
print(my2DList)
print(my2DList[3][3][1][1]) #print last element of sub which is the last element of last sublist in my2DList([3]-list at index 3 of my2DList,[3]-list at index 3 of sublist which is sub,[1]-list at index 1 of sub,[1]-element at index 1 of 2nd sublist in sub)

Name=input("Enter name: ")
Month=int(input("Enter month: "))
Date=int(input("Enter date: "))
Year=int(input("Enter year: "))
Address=input("Enter address: ")
Home=input("Enter home number: ")
Cell=input("Enter cell number: ")
myList=[Name,[Month,Date,Year],Address,[Home,Cell]]
print(myList)

