#ball pit problem
def BallPit(Radius, Height):
    return 3.14*(Radius*Radius)*Height
def Ball(Radius):
    return (4/3)*3.14*(Radius*Radius*Radius)

#main program
BallsNeeded = BallPit(1, 0.2) / Ball(0.05) * 0.75
print("You'll need", BallsNeeded, "balls.")






