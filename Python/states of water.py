#States of water problem
#Subroutine to determine state of water
def StateofWater(Number):
    if Number >= 100:
        return "Gaseous"
    elif Number >= 1 and Number <= 99:
        return "Liquid"
    elif Number < 1:
        return "Solid"

#Main program
print(StateofWater(float(37.2)))



