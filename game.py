import random
"""A number-guessing game."""

# Put your code here
randomNumber = random.randint(1, 100)
guessNumber = 0
guessCounter = 0
name = input('hello what is your name:')
print('choose a random number between 1 and 100')
while (randomNumber != int(guessNumber)):
    guessNumber = input('what is your guess: ')
    trueNumber = int(guessNumber)
    if trueNumber > randomNumber :
        guessCounter += 1
        print('number is lower')
    if trueNumber < randomNumber :
        guessCounter += 1
        print('number is higher')
else: 
    print('congrates on guessing correctly ' + name + ' you did it with ' + str(guessCounter) + ' guesses')
