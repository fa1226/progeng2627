#Career quote problem
#Subroutine to take the job in and output a quote
def CareerQuote(Job):
    if Job == str('Engineer'):
        return "The engineer has been, and is, a maker of history."
    elif Job == str('Developer'):
        return "Logical thinking, passion, and perseverance is the paint on your palette."
    elif Job == str('Analyst'):
        return "Seeing what other people can't see gives you great vision."
    else:
        return "Sorry, we could not find a quote for your job."

#Main program
print(CareerQuote(str('Engineer')))





