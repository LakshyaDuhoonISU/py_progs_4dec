#tuple methods
tuple=(0,1,2,4,5,5,4)
print(tuple.count(4)) #returns the number of times "4" has occurred in tuple

print(tuple[1]) #returns element of index 1 in the tuple

print(tuple.index(4)) #returns the first index of the value "4" in the tuple

'''tuple[1]=6
print(tuple)''' #error as tuple is immutable

'''for i in tuple:
    print(i)  #print every element of the tuple

thistuple=("apple","banana","cherry")
if "apple" in thistuple: #check if an element is in the tuple
    print("Yes,'apple' is in the fruits table")

print(len(thistuple)) #print the number of elements in the tuple

thistuple=(["apple","banana","cherry"]) #insert the list in tuple so that we can change the elements in the tuple
thistuple[0]="banana"
print(thistuple)'''

thistuple=("apple","banana","cherry","watermelon","carrot","apple")
print(thistuple.index("apple",1,6)) #returns the first occurence of the value from range index 1 to 5(6-1)
