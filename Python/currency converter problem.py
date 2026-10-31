#Currency converter problem
#Subroutine to take in parameters and convert currency
def CurrencyConverter(Pounds, NameofCurrency):
    if NameofCurrency == str('Dollar'):
        return Pounds * 1.21
    elif NameofCurrency == str('Euro'):
        return Pounds * 1.14
    elif NameofCurrency == str('Yuan'):
        return Pounds * 8.44
    elif NameofCurrency == str('Yen'):
        return Pounds * 159.96
    

#Main program
output = (CurrencyConverter(float(input("Number of pounds:")), str(input("Type of currency:"))))
rounded = round(output, 2)
print("The converted amount rounded to 2d.p is", rounded)
 


