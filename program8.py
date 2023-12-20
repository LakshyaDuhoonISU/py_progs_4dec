#wap to manage a library catalogue(use control structures to add,search for and check out books and maintain libraries inventory)
print("Welcome to ABC library")
x=[]
while True:
    d=int(input("Enter\n1.Adding Books\n2.Check Inventory\n3.Search for books\n4.Exit\n"))
    if d==1:
        a=input("Enter book name: ")
        x.append(a)
        print("Your books are:",x)
    elif d==2:
        if x==[]:
            print("No books available!")
        else:
            print("Your books are:",x)
    elif d==3:
        e=input("Enter book to search for: ")
        if e in x:
            print("Book found")
        else:
            print("Book not found")
    elif d==4:
        print("Thank you for visiting. Have a nice day ahead.")
        break
    else:
        print("Wrong option")