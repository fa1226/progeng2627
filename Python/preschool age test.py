# Selection commands

# Subroutine to validate month
def ValidAge(Age):
    if Age >= 2 and Age <= 5:
        print("Your child is eligible for preschool.")
    else:
        print("Your child is not eligible for preschool.") 

# Main program
ValidAge(7)
