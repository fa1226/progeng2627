#day format problem
#subroutine to determine format and day
def DayFormat(Number, Format):
    if Number == 1 and Format == str('day'):
        return "Monday"
    elif Number == 1 and Format == str('shortday'):
        return "Mon"
    elif Number == 1 and Format == str('char'):
        return "M"
    elif Number == 2 and Format == str('day'):
        return "Tuesday"
    elif Number == 2 and Format == str('shortday'):
        return "Tue"
    elif Number == 2 and Format == str('char'):
        return "Tu"
    elif Number == 3 and Format == str('day'):
        return "Wednesday"
    elif Number == 3 and Format == str('shortday'):
        return "Wed"
    elif Number == 3 and Format == str('char'):
        return "W"
    elif Number == 4 and Format == str('day'):
        return "Thursday"
    elif Number == 4 and Format == str('shortday'):
        return "Thu"
    elif Number == 4 and Format == str('char'):
        return "Th"
    elif Number == 5 and Format == str('day'):
X        return "Friday"
    elif Number == 5 and Format == str('shortday'):
        return "Fri"
    elif Number == 5 and Format == str('char'):
        return "F"
    elif Number == 6 and Format == str('day'):
        return "Saturday"
    elif Number == 6 and Format == str('shortday'):
        return "Sat"
    elif Number == 6 and Format == str('char'):
        return "Sa"
    elif Number == 7 and Format == str('day'):
        return "Sunday"
    elif Number == 7 and Format == str('shortday'):
        return "Sun"
    elif Number == 7 and Format == str('char'):
        return "Su"
    
#main program 
print(DayFormat(int(input("Day number:")), str(input("Format:"))))


