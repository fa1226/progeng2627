#task 1
import random
tries = 0
correct = False
num = random.randint(1, 64)
while correct == False:
    guess = int(input("Guess: "))
    if guess > num:
        print("Too high")
        tries = tries + 1
    elif guess < num:
        print("Too low")
        tries = tries + 1
    elif guess == num:
        tries = tries + 1
        correct = True
        print("Well done!")
        print("You took", tries, "tries")


