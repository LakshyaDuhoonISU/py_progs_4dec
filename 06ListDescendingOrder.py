#wap to arrange list in descending order
a=[5,3,7,1,8,2]
b=0
c=len(a)-1
for i in range(len(a)-1):
    for j in range(len(a)-i-1):
        if a[j]<a[j+1]:
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp
print(a)
