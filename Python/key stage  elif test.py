# Selection commands

# Subroutine to output Key Stage
def YearGroup(Year):
    if Year <0:
        print("Error")
    elif Year == 0:
        print("Reception")
    elif Year >= 1 and Year <=2:
        print("Key Stage 1")
    elif Year >= 3 and Year <=6:
        print("Key Stage 2")
    elif Year >= 7 and Year <10:
        print("Key Stage 3")
    elif Year >=10 and Year <12:
        print("Key Stage 4") 
    elif Year >=12 and Year <=13:
        print("Sixth Form")
    elif Year > 13:
        print("Post-school")

# Main program
YearGroup(19)


z
