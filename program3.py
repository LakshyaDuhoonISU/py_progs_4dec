#dictionary operations(key:value pairs)
x={1:"x",2:"y",3:"z",4:[1,2,3],5:{1:"x",2:"y",3:"z"}}
print(x)
print(x[3]) #print the value of key 3
print(x[4])
print(x[5])
print(x[5][1]) #print value of key 1 of the dictionary inside the key 5 in dictionary d
del[x[5][2]] #delete key 2 of the dictionary inside the key 5 in dictionary d
print(x)