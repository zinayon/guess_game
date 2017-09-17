#This is a guess the number game.
import random

guessesTaken = 0

print ('System: Hello! What is your name?')
myName = input("Me: ")
number = random.randint (1, 20)

print('System: Well, '+myName+', I am thinking of a number between 1 and 20')

while guessesTaken < 6:

    guess = int(input("System: Take a guess: "))
    guessesTaken = guessesTaken + 1

    if guess < number:
        print('Your guess is too low.')
    if guess > number:
        print ('System: Your guess is too high')
    if guess == number:
        break
if guess == number:
    guessesTaken = str(guessesTaken)
    print('System: Good job,'+myName+'! You guessed my number in '+guessesTaken+' guesses.')
if guess !=number:
    number = str(number)
    print ('System: Nope. The number i was thinking was '+number)
