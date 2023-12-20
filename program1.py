#list operations(is mutable)
'''x=[1,"hello",23,(3+4j)] 
print(x) #printing list
print(x[4:2:-1]) #printing list in reverse order
'''
x=[1,2,3]
y=x #y is assigned the contents of x
print(y)
x[1]=15 #reassigning element in x(which will also be changed in y)
print(x)
print(y)
x.append(56) #adding element in x at the end(which will also be changed in y)
y.append(43) #adding element in y at the end(which will also be changed in x)
print(x)
print(y)
z=x.append(12)
print(y)
print(x)
print(z) #returns None (as append operation returns None)
x=x+[2,3] #list concatenation in x doesn't change values in y
print(x)

