#name separator problem
#subroutine to separate full name into two strings
def Separate(FullName):
    space = FullName.find(" ")
    Forename = FullName[0:space]
    Surname = FullName[space+1:]
    print(Forename)
    print(Surname)

#main program
FullName = str(input("Full name:"))
Separate(FullName)


