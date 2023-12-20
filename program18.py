#dictionary methods
d={1:"abc",2:"xyz","abc":[3,1]}
d1={"abc":1,2:"xyz",3:[1,2]}
print(d.keys()) #returns keys from the dictionary

print(d.values()) #returns values from the dictionary

d.pop(1) #removes the key value pair of key "1" from the dictionary
print(d)

d.update(d1) #merges key value pairs from dictionary d1 to another dictionary d
print(d)

d.clear() #removes all the pairs from the dictionary
print(d)

