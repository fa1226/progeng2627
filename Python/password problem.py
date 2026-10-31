password = str(input("Password: "))
while len(str(password))!=6:
    print("Invalid password, try again")
    password = str(input("Password: "))
print("Valid password.")
