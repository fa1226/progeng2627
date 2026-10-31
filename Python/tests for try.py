# Number data types

# Subroutine to calculate VAT
def VAT(Total, Rate):
    if Rate == str('Standard'):
        return Total * 0.2
    elif Rate == str('Reduced'):
        return Total * 0.05
    elif Rate == str('Zero'):
        return Total * 0

# Main program
Total = 99.99
Rate = str(input("VAT Rate:"))
ValueAddedTax = VAT(Total, Rate)
ToPay = Total + ValueAddedTax
print("Total £{:.2f}, VAT £{:.2f}, To pay £{:.2f}".format(Total, ValueAddedTax, ToPay))







                                                          
