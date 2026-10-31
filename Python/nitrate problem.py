#Nitrate problem
#Subroutine to determine carbon dose
def CarbonDose(Nitrate):
    if Nitrate > 10:
        return "3"
    elif Nitrate >= 2.5 and Nitrate < 10:
        return "2"
    elif Nitrate >= 1 and Nitrate < 2.5:
        return "1"
    else:
        return "0.5"

#Main program
nitrate = float(input("Amount of nitrate:"))
output = CarbonDose(nitrate)
print("For", nitrate, "nitrate dose you need", output,"ml of carbon.")




