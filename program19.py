#wap that scans an email address and forms a tuple of user name and domain of 5 useremails
for i in range(5):
    a=input("Enter your email address: ")
    if "@" in a:
        b=(a.split("@"))
        c=(b[0])
        d=(b[1])
        print("User name:",c)
        print("Domain:",d)
    else:
        print("Wrong email address entered")
        break
