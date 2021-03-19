# guess a randomly generated number


input("Press Enter to set the range and guess the value of the randomly generated number. \n\nHave fun! :)")

from numpy import random
max = input("\n\nInput largest number: ")
randomgen = random.randint(0, max)
correctnum = randomgen
isnumbercorrect = bool(False)
while isnumbercorrect == False:
    guess = int(input("\nWhat is the number? "))
    if guess == correctnum:
        print("You guessed right!")
        isnumbercorrect = bool(True)
    else:
        if guess < correctnum:
                print("The number you entered is too low! Try again D:")
        if guess > correctnum:
                print("The number you entered is too high! Try again D:")

print("\n\nGame Over. Press run to replay!")
