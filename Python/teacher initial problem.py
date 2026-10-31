#teacher initial problem
#subroutine to take in teacher's full name and return initials
def Initials(Forename, Middle, Surname):
    initial1 = Forename[0:1]
    if Middle == "":
        initial2 = "Z"
    else:
        initial2 = Middle[0:1]
    initial3 = Surname[0:1]
    initials = initial1.upper() + initial2.upper() + initial3.upper()
    return initials

#main program
Forename = str(input("First name:"))
Middle = str(input("Middle name:"))
Surname = str(input("Last name:"))
print(Initials(Forename, Middle, Surname))
    


