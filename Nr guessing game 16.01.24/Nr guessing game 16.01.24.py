# import random
import random

# welcome text
print("Guess the secret random nr from 0 to 10!")

# variables
guess = input("Type a nr : ")
random_nr = random.randint(0,10)

# check if guess is a digit and if more than 0, otherwise quit program
if guess.isdigit():
    guess = int(guess)

    if guess <= 0:
        print("Guess higher than zero")
        quit()
else:
    print("Pick a nr next time")
    quit()

# compare guess to random nr
while guess != random_nr:
    if guess < random_nr:
        print("Too low")
    if guess > random_nr:
        print("Too high")
    if guess == random_nr:
        print("Well done")
    break

# tell user what the secret random nr was
print("The random nr was actually", random_nr, "and not", guess)
