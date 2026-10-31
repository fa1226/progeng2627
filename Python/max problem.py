#Max problem
#Subroutine to determine which number is bigger and output it
def MaxNumber(Number1, Number2):
    if Number1 > Number2:
        return Number1
    elif Number1 < Number2:
        return Number2
    elif Number1 == Number2:
        return "Both numbers are the same."

#Main program
print(MaxNumber(18,11))


