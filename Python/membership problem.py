#membership problem
hours = int(input("Session length in hours:"))
cost = hours * 5
member = str(input("Are you a member?"))
if member == str("Yes") or member == str("yes"):
    age = int(input("Age:"))
    if age >= 65:
        total = cost * 0.5
        print("You are eligible for a 50% senior discount. Amount to pay: £", total)
    elif age > 16 and age < 65:
        total = cost * 0.9
        print("You are eligible for a 10% adult discount. Amount to pay: £", total)
    elif age <= 16:
        total = cost * 0.75
        print("You are eligible for a 25% child discount. Amount to pay: £", total)
else:
    print("Amount to pay: £", cost)
        
