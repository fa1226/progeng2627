#valid address problem
#subroutine to check validity of email address
def Valid(Email):
    dot = "."
    at = "@"
    if at in Email and dot in Email:
        return True
    else:
        return False

#main program
Email = str(input("Email address:"))
print(Valid(Email))
